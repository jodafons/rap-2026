import os
import json
from typing import List, Union, Tuple, Optional
import numpy as np
from PIL import Image
from loguru import logger

class ImageMixer:
    """
    A class responsible for mixing a list of source images to create an ICA exercise.
    Supports resizing, adding noise, and mixing per RGB channel or converting to grayscale.
    """
    def __init__(
        self,
        size: Optional[Tuple[int, int]] = None,
        add_noise: bool = False,
        noise_level: float = 0.05,
        mix_by_channel: bool = True,
        mixing_matrix: Optional[Union[np.ndarray, List[List[float]]]] = None,
        seed: Optional[int] = None
    ):
        """
        Initializes the ImageMixer class.

        Args:
            size (Tuple[int, int], optional): Target size (width, height) to resize all images.
                If None, images are resized to match the size of the first image in the input list.
            add_noise (bool): Whether to add Gaussian noise to the mixed images.
            noise_level (float): The standard deviation of the Gaussian noise, relative to the [0.0, 1.0] range.
            mix_by_channel (bool): If True, applies mixing per RGB channel independently (using the same mixing matrix).
                If False, converts all source images to grayscale before mixing.
            mixing_matrix (np.ndarray, optional): Custom mixing matrix of shape (M, N) where M is the number of
                mixed output images and N is the number of input source images. If None, a random invertible
                mixing matrix will be generated.
            seed (int, optional): Random seed for reproducibility of matrix generation and noise addition.
        """
        self.size = size
        self.add_noise = add_noise
        self.noise_level = noise_level
        self.mix_by_channel = mix_by_channel
        self.seed = seed
        
        if mixing_matrix is not None:
            self.mixing_matrix = np.array(mixing_matrix, dtype=np.float32)
        else:
            self.mixing_matrix = None
            
        self._actual_size = None
        self.sources_ = []
        self.mixing_matrix_ = None
        self.mixed_images_raw_ = []
        self.mixed_images_ = []

    def _load_image(self, img_input: Union[str, os.PathLike, Image.Image, np.ndarray]) -> np.ndarray:
        """
        Loads an image from a path, PIL Image, or numpy array.
        Resizes it and converts it to the target color mode (RGB or Grayscale).
        Returns a float32 numpy array in the range [0.0, 1.0].
        """
        if isinstance(img_input, (str, os.PathLike)):
            img = Image.open(img_input)
        elif isinstance(img_input, Image.Image):
            img = img_input
        elif isinstance(img_input, np.ndarray):
            # If it's a float array, scale to [0, 255] and cast to uint8
            if np.issubdtype(img_input.dtype, np.floating):
                scaled = (np.clip(img_input, 0.0, 1.0) * 255.0).round().astype(np.uint8)
            else:
                scaled = img_input.astype(np.uint8)
            
            # Determine mode based on shape
            if len(scaled.shape) == 3 and scaled.shape[2] == 3:
                img = Image.fromarray(scaled, mode="RGB")
            else:
                img = Image.fromarray(scaled, mode="L")
        else:
            raise TypeError(f"Unsupported image input type: {type(img_input)}")

        # Resize if actual_size has been resolved
        if self._actual_size is not None:
            try:
                resample_filter = Image.Resampling.LANCZOS
            except AttributeError:
                resample_filter = Image.LANCZOS
            img = img.resize(self._actual_size, resample=resample_filter)

        # Color format conversion
        if self.mix_by_channel:
            if img.mode != "RGB":
                img = img.convert("RGB")
        else:
            if img.mode != "L":
                img = img.convert("L")

        # Convert to numpy array in [0.0, 1.0] range
        arr = np.array(img, dtype=np.float32) / 255.0
        return arr

    def _generate_well_conditioned_matrix(self, m: int, n: int) -> np.ndarray:
        """
        Generates a random mixing matrix of shape (m, n) with a reasonable condition number.
        For non-square matrices (m != n), checks singular value ratio.
        """
        rng = np.random.default_rng(self.seed)
        max_attempts = 200
        best_A = None
        best_cond = float('inf')
        
        for _ in range(max_attempts):
            # Generate random numbers in [-1.5, -0.5] U [0.5, 1.5] to avoid numbers near zero
            A = rng.uniform(0.5, 1.5, size=(m, n))
            signs = rng.choice([-1, 1], size=(m, n))
            A = A * signs
            
            # Compute condition number
            if m == n:
                cond = np.linalg.cond(A)
            else:
                _, s, _ = np.linalg.svd(A)
                cond = s[0] / s[-1] if s[-1] > 1e-6 else float('inf')
            
            # Target a condition number between 1.2 and 8.0 for a stable but non-trivial mix
            if 1.2 < cond < 8.0:
                logger.debug(f"Generated mixing matrix of shape {A.shape} with condition number {cond:.4f}")
                return A
            
            if cond < best_cond:
                best_cond = cond
                best_A = A
                
        logger.warning(f"Could not find a matrix with condition number < 8.0 after {max_attempts} attempts. "
                       f"Using best matrix found with condition number {best_cond:.4f}")
        return best_A

    def mix(
        self,
        images: List[Union[str, os.PathLike, Image.Image, np.ndarray]],
        num_mixtures: Optional[int] = None
    ) -> List[np.ndarray]:
        """
        Applies mixing to the input images and returns the mixed images.

        Args:
            images (List): A list of images, either file paths, PIL Images, or numpy arrays.
            num_mixtures (int, optional): The number of mixed output images to generate.
                Defaults to the number of input images. Ignored if a custom mixing matrix was provided.

        Returns:
            List[np.ndarray]: The list of mixed images, each as a numpy array in the range [0.0, 1.0].
        """
        if not images:
            raise ValueError("Input image list cannot be empty.")

        n = len(images)

        # 1. Determine target size from the first image if not pre-specified
        if self.size is None:
            first_input = images[0]
            if isinstance(first_input, (str, os.PathLike)):
                with Image.open(first_input) as img:
                    self._actual_size = img.size
            elif isinstance(first_input, Image.Image):
                self._actual_size = first_input.size
            elif isinstance(first_input, np.ndarray):
                h, w = first_input.shape[:2]
                self._actual_size = (w, h)
            else:
                raise TypeError(f"Unsupported image type for first element: {type(first_input)}")
        else:
            self._actual_size = self.size

        logger.debug(f"Resolved mixing size to: {self._actual_size}")

        # 2. Load all source images
        self.sources_ = [self._load_image(img) for img in images]

        # 3. Determine and validate mixing matrix
        if self.mixing_matrix is not None:
            m = self.mixing_matrix.shape[0]
            if self.mixing_matrix.shape[1] != n:
                raise ValueError(
                    f"Custom mixing_matrix has {self.mixing_matrix.shape[1]} columns, "
                    f"but expected {n} (matching the number of source images)."
                )
            A = self.mixing_matrix
        else:
            m = num_mixtures if num_mixtures is not None else n
            A = self._generate_well_conditioned_matrix(m, n)

        self.mixing_matrix_ = A

        # 4. Perform the linear mixture
        # Stack source images to shape (N, H, W, 3) or (N, H, W)
        S_stacked = np.stack(self.sources_, axis=0)

        if self.mix_by_channel:
            # S_stacked is (N, H, W, 3)
            # mixed_raw has shape (M, H, W, 3)
            mixed_raw = np.einsum('ij,jhwc->ihwc', A, S_stacked)
        else:
            # S_stacked is (N, H, W)
            # mixed_raw has shape (M, H, W)
            mixed_raw = np.einsum('ij,jhw->ihw', A, S_stacked)

        self.mixed_images_raw_ = [mixed_raw[i] for i in range(m)]

        # 5. Normalize mixed images and add noise if requested
        self.mixed_images_ = []
        seed_seq = np.random.SeedSequence(self.seed) if self.seed is not None else np.random.SeedSequence()
        child_seeds = seed_seq.spawn(m)

        for i in range(m):
            img_raw = self.mixed_images_raw_[i]
            
            # Normalize to [0.0, 1.0] range
            img_min = img_raw.min()
            img_max = img_raw.max()
            if img_max > img_min:
                normalized = (img_raw - img_min) / (img_max - img_min)
            else:
                normalized = np.zeros_like(img_raw)

            # Add noise if requested
            if self.add_noise and self.noise_level > 0:
                rng = np.random.default_rng(child_seeds[i])
                noise = rng.normal(0, self.noise_level, size=normalized.shape)
                normalized = np.clip(normalized + noise, 0.0, 1.0)

            self.mixed_images_.append(normalized)

        return self.mixed_images_

    def get_mixed_images_as_pil(self) -> List[Image.Image]:
        """
        Returns the mixed images as PIL Image objects.
        """
        if not self.mixed_images_:
            raise ValueError("You must call mix() first.")

        pil_images = []
        for img_arr in self.mixed_images_:
            uint8_arr = (img_arr * 255.0).round().astype(np.uint8)
            if self.mix_by_channel:
                img = Image.fromarray(uint8_arr, mode="RGB")
            else:
                img = Image.fromarray(uint8_arr, mode="L")
            pil_images.append(img)
        return pil_images

    def get_sources_as_pil(self) -> List[Image.Image]:
        """
        Returns the processed original source images as PIL Image objects.
        """
        if not self.sources_:
            raise ValueError("You must call mix() first.")

        pil_images = []
        for img_arr in self.sources_:
            uint8_arr = (img_arr * 255.0).round().astype(np.uint8)
            if self.mix_by_channel:
                img = Image.fromarray(uint8_arr, mode="RGB")
            else:
                img = Image.fromarray(uint8_arr, mode="L")
            pil_images.append(img)
        return pil_images

    def save_mixed_images(self, output_dir: str, prefix: str = "mixed", format: str = "png") -> List[str]:
        """
        Saves the mixed images to the specified directory.

        Returns:
            List[str]: A list of file paths to the saved images.
        """
        os.makedirs(output_dir, exist_ok=True)
        pil_imgs = self.get_mixed_images_as_pil()
        paths = []
        for i, img in enumerate(pil_imgs):
            filename = f"{prefix}_{i}.{format}"
            path = os.path.join(output_dir, filename)
            img.save(path)
            paths.append(path)
        logger.info(f"Saved {len(pil_imgs)} mixed images to {output_dir}")
        return paths

    def save_sources(self, output_dir: str, prefix: str = "source", format: str = "png") -> List[str]:
        """
        Saves the processed original source images to the specified directory.

        Returns:
            List[str]: A list of file paths to the saved images.
        """
        os.makedirs(output_dir, exist_ok=True)
        pil_imgs = self.get_sources_as_pil()
        paths = []
        for i, img in enumerate(pil_imgs):
            filename = f"{prefix}_{i}.{format}"
            path = os.path.join(output_dir, filename)
            img.save(path)
            paths.append(path)
        logger.info(f"Saved {len(pil_imgs)} source images to {output_dir}")
        return paths

    def save_metadata(self, filepath: str):
        """
        Saves the mixing configurations and the mixing matrix to a JSON file.
        """
        if self.mixing_matrix_ is None:
            raise ValueError("You must call mix() first.")

        metadata = {
            "size": list(self.size) if self.size is not None else None,
            "actual_size": list(self._actual_size) if self._actual_size is not None else None,
            "add_noise": self.add_noise,
            "noise_level": self.noise_level,
            "mix_by_channel": self.mix_by_channel,
            "mixing_matrix": self.mixing_matrix_.tolist(),
            "seed": self.seed
        }

        # Make sure parent directory exists
        dirname = os.path.dirname(os.path.abspath(filepath))
        if dirname:
            os.makedirs(dirname, exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=4)
        logger.info(f"Saved mixture metadata to {filepath}")
