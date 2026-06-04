import unittest
import os
import json
import shutil
import tempfile
import numpy as np
from PIL import Image
from mixer.image_mixer import ImageMixer

class TestImageMixer(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for output files
        self.test_dir = tempfile.mkdtemp()
        
        # Generate synthetic source images for testing (3 images of size 50x50)
        self.size = (50, 50)
        self.sources = []
        
        # Image 1: horizontal stripe
        img1 = np.zeros((50, 50, 3), dtype=np.uint8)
        img1[10:20, :, 0] = 255
        img1[20:30, :, 1] = 255
        img1[30:40, :, 2] = 255
        self.sources.append(img1)
        
        # Image 2: vertical stripe
        img2 = np.zeros((50, 50, 3), dtype=np.uint8)
        img2[:, 10:20, 0] = 255
        img2[:, 20:30, 1] = 255
        img2[:, 30:40, 2] = 255
        self.sources.append(img2)
        
        # Image 3: diagonal stripe (represented as PIL Image)
        img3_arr = np.zeros((50, 50, 3), dtype=np.uint8)
        for i in range(50):
            img3_arr[i, i, :] = 255
        self.sources.append(Image.fromarray(img3_arr))

    def tearDown(self):
        # Remove temporary directory
        shutil.rmtree(self.test_dir)

    def test_initialization(self):
        mixer = ImageMixer(size=(100, 100), add_noise=True, noise_level=0.1, mix_by_channel=False, seed=42)
        self.assertEqual(mixer.size, (100, 100))
        self.assertTrue(mixer.add_noise)
        self.assertEqual(mixer.noise_level, 0.1)
        self.assertFalse(mixer.mix_by_channel)
        self.assertEqual(mixer.seed, 42)

    def test_random_matrix_generation(self):
        mixer = ImageMixer(seed=42)
        # Generate mixing matrix for 3 sources and 3 mixtures
        A = mixer._generate_well_conditioned_matrix(3, 3)
        self.assertEqual(A.shape, (3, 3))
        # Ensure it is invertible
        det = np.linalg.det(A)
        self.assertNotEqual(det, 0.0)
        # Ensure condition number is reasonable
        cond = np.linalg.cond(A)
        self.assertLess(cond, 10.0)

    def test_mix_rgb(self):
        mixer = ImageMixer(size=self.size, mix_by_channel=True, seed=123)
        mixed = mixer.mix(self.sources)
        
        # We passed 3 sources, default mixtures is 3
        self.assertEqual(len(mixed), 3)
        self.assertEqual(mixed[0].shape, (50, 50, 3))
        
        # Ensure values are in [0, 1] range
        for img in mixed:
            self.assertTrue(np.all(img >= 0.0))
            self.assertTrue(np.all(img <= 1.0))
            
        # Check source shapes
        self.assertEqual(len(mixer.sources_), 3)
        self.assertEqual(mixer.sources_[0].shape, (50, 50, 3))
        
        # Check mixing matrix shape
        self.assertEqual(mixer.mixing_matrix_.shape, (3, 3))

    def test_mix_grayscale(self):
        mixer = ImageMixer(size=self.size, mix_by_channel=False, seed=123)
        mixed = mixer.mix(self.sources)
        
        self.assertEqual(len(mixed), 3)
        self.assertEqual(mixed[0].shape, (50, 50))
        
        # Check source shapes (should be grayscale, so 2D (50, 50))
        self.assertEqual(mixer.sources_[0].shape, (50, 50))

    def test_custom_mixing_matrix(self):
        custom_A = np.array([
            [1.0, 0.5, -0.2],
            [-0.3, 0.8, 1.2]
        ])
        mixer = ImageMixer(size=self.size, mixing_matrix=custom_A)
        mixed = mixer.mix(self.sources)
        
        # Num mixtures is determined by shape of custom_A (2 mixtures, 3 sources)
        self.assertEqual(len(mixed), 2)
        self.assertEqual(mixer.mixing_matrix_.shape, (2, 3))
        np.testing.assert_allclose(mixer.mixing_matrix_, custom_A, rtol=1e-5)

    def test_autosize(self):
        # Initialise with size=None
        mixer = ImageMixer(size=None)
        mixed = mixer.mix(self.sources)
        
        # Since first source is 50x50, size should default to (50, 50)
        self.assertEqual(mixer._actual_size, (50, 50))
        self.assertEqual(mixed[0].shape, (50, 50, 3))

    def test_add_noise(self):
        # Mix without noise
        mixer_clean = ImageMixer(size=self.size, add_noise=False, seed=42)
        mixed_clean = mixer_clean.mix(self.sources)
        
        # Mix with noise
        mixer_noisy = ImageMixer(size=self.size, add_noise=True, noise_level=0.1, seed=42)
        mixed_noisy = mixer_noisy.mix(self.sources)
        
        # They should be different
        self.assertFalse(np.array_equal(mixed_clean[0], mixed_noisy[0]))

    def test_saving_and_metadata(self):
        mixer = ImageMixer(size=self.size, add_noise=True, noise_level=0.05, seed=42)
        mixer.mix(self.sources)
        
        # Save mixed images
        mixed_paths = mixer.save_mixed_images(self.test_dir, prefix="test_mixed")
        self.assertEqual(len(mixed_paths), 3)
        for path in mixed_paths:
            self.assertTrue(os.path.exists(path))
            
        # Save sources
        source_paths = mixer.save_sources(self.test_dir, prefix="test_source")
        self.assertEqual(len(source_paths), 3)
        for path in source_paths:
            self.assertTrue(os.path.exists(path))
            
        # Save metadata
        metadata_path = os.path.join(self.test_dir, "metadata.json")
        mixer.save_metadata(metadata_path)
        self.assertTrue(os.path.exists(metadata_path))
        
        # Verify metadata contents
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
        self.assertEqual(metadata["size"], list(self.size))
        self.assertTrue(metadata["add_noise"])
        self.assertEqual(metadata["noise_level"], 0.05)
        self.assertTrue(metadata["mix_by_channel"])
        self.assertEqual(len(metadata["mixing_matrix"]), 3)

if __name__ == '__main__':
    unittest.main()
