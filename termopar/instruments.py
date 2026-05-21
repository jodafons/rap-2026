__all__ = [
    'Sensor',
    'AmpOp',
    'ADC',
    'Filter',
    'Temperature',
]

from typing import Tuple, Union
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import scipy.stats as stats
from termopar.units import *


class Sensor:
    """
    Simulates a thermocouple sensor with noise injection.
    """

    def __init__(self, 
                 white_noise_V : float,
                 amp_noise_V : float,
                 f_noise_Hz : float,
                 sens_termopar : float,
                 amp_harm_V : float = 0.0,
                 amp_drift_V : float = 0.0,
                ) -> None:
        """
        Initializes the Sensor with noise and sensitivity parameters.

        Args:
            white_noise_V (float): Standard deviation of white noise in Volts.
            amp_noise_V (float): Amplitude of the network noise in Volts.
            f_noise_Hz (float): Frequency of the network noise in Hertz.
            sens_termopar (float): Sensitivity of the thermocouple in V/°C.
            amp_harm_V (float): Amplitude of 2nd harmonic noise (120Hz).
            amp_drift_V (float): Amplitude of thermal drift noise (0.05Hz).
        """
        self.white_noise_V = white_noise_V
        self.amp_noise_V = amp_noise_V
        self.f_noise_Hz = f_noise_Hz
        self.sens_termopar = sens_termopar
        self.amp_harm_V = amp_harm_V
        self.amp_drift_V = amp_drift_V

    def run(self, 
            t : np.ndarray,
            T : float, 
           ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Simulates the sensor reading over a given time array.

        Args:
            t (np.array): Time array.
            T (float): True temperature value.

        Returns:
            tuple: A tuple containing the time array and the output voltage array with noise.
        """
        # real temperature value
        v = T*self.sens_termopar
        # noise injection
        white_noise = np.random.normal(0, self.white_noise_V, len(t))
        network_noise = self.amp_noise_V * np.sin( 2*np.pi*self.f_noise_Hz*t)
        harm_noise = self.amp_harm_V * np.sin( 2*np.pi*120*t)
        drift_noise = self.amp_drift_V * np.sin( 2*np.pi*0.05*t)
        v_out = v + white_noise + network_noise + harm_noise + drift_noise
        return t, v_out

class AmpOp:
    """
    Simulates an operational amplifier with offset and saturation.
    """
    def __init__(self, 
                 A_V : float = 100, 
                 v_offset : float = 15*mV, 
                 v_min: float = 0*V, 
                 v_max: float = 5*V 
                ) -> None:
        """
        Initializes the operational amplifier.

        Args:
            A_V (float): Voltage gain. Defaults to 100.
            v_offset (float): Offset voltage. Defaults to 15 mV.
            v_min (float): Minimum saturation voltage. Defaults to 0 V.
            v_max (float): Maximum saturation voltage. Defaults to 5 V.
        """
        self.A_V = A_V
        self.v_offset = v_offset
        self.v_min = v_min
        self.v_max = v_max

    def run(self, v_in: Union[np.ndarray, float]) -> Union[np.ndarray, float]:
        """
        Amplifies the input voltage and applies offset and clipping.

        Args:
            v_in (np.array or float): Input voltage.

        Returns:
            np.array or float: Amplified and clipped output voltage.
        """
        # amplification
        v_out = v_in * self.A_V + self.v_offset
        v_out = np.clip (v_out , self.v_min, self.v_max)
        return v_out

class ADC:
    """
    Simulates an Analog-to-Digital Converter.
    """

    def __init__(self, 
                 n_bits : int,
                 fs : float, 
                 fs_real_world : float,
                 v_min : float = 0*V,
                 v_max : float = 3.3*V
                ) -> None:
        """
        Initializes the ADC.

        Args:
            n_bits (int): Resolution in bits.
            fs (float): Sampling frequency of the ADC in Hz.
            fs_real_world (float): Sampling frequency of the continuous input signal in Hz.
            v_min (float): Minimum voltage limit. Defaults to 0 V.
            v_max (float): Maximum voltage limit. Defaults to 3.3 V.
        """
        self.n_bits = n_bits
        self.v_min = v_min
        self.v_max = v_max
        self.fs = fs
        self._step = 1 if int(fs_real_world/fs) < 1 else int(fs_real_world/fs)
    
    def run(self, t: np.ndarray, v_in: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Digitizes the input signal in time and amplitude.

        Args:
            t (np.array): Time array of the input signal.
            v_in (np.array): Input voltage signal.

        Returns:
            tuple: A tuple containing the downsampled time array and the digitized voltage array.
        """

        n = t[::self._step]
        v_n_in = v_in[::self._step]
        steps  = 2**self.n_bits
        quantum = (self.v_max - self.v_min) / steps
        v_n_in = np.clip(v_n_in, self.v_min, self.v_max)
        word = np.floor((v_n_in - self.v_min) / quantum).astype(int)
        word = np.clip(word, 0, steps - 1)
        v_out_digit = self.v_min + word * quantum + (quantum / 2)
        return n, v_out_digit

class Filter:
    """
    Simulates a digital low-pass Butterworth filter.
    """
    def __init__(self, fs : float, f_cut : float, order : int = 4) -> None:
        """
        Initializes the Filter.

        Args:
            fs (float): Sampling frequency in Hz.
            f_cut (float): Cutoff frequency in Hz.
            order (int): Filter order. Defaults to 4.
        """
        self.fs = fs
        self.f_cut = f_cut
        self.order = order

    def run(self, v_in: np.ndarray) -> np.ndarray:
        """
        Filters the input signal.

        Args:
            v_in (np.array): Input voltage signal.

        Returns:
            np.array: Filtered voltage signal.
        """
        nyquist = 0.5 * self.fs
        f_cut_norm = self.f_cut / nyquist
        b, a = signal.butter(self.order, f_cut_norm, btype='low')
        return signal.lfilter(b, a, v_in)
        

class Temperature:
    """
    Converts a processed voltage signal back to temperature.
    """
    def __init__( self,
                  sens_termopar : float,
                  A_V : float = 100,
                  v_offset : float = 15*mV
                ) -> None:
        """
        Initializes the Temperature converter.

        Args:
            sens_termopar (float): Sensitivity of the thermocouple in V/°C.
            A_V (float): Voltage gain of the amplifier. Defaults to 100.
            v_offset (float): Offset voltage applied before. Defaults to 15 mV.
        """
        self.sens_termopar = sens_termopar
        self.A_V = A_V
        self.v_offset = v_offset
                  
    def run(self, v_in: Union[np.ndarray, float]) -> Union[np.ndarray, float]:
        """
        Converts input voltage to temperature.

        Args:
            v_in (np.array or float): Input voltage.

        Returns:
            np.array or float: Reconstructed temperature.
        """
        T = v_in - self.v_offset
        T = T / (self.A_V * self.sens_termopar)
        return T
