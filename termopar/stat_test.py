__all__ = [
    'ChiSquare'
]

from typing import Tuple, Dict, Any, Callable
import numpy as np
from scipy.optimize import curve_fit
from scipy import stats
import matplotlib.pyplot as plt

def normal(x: np.ndarray, mean: float, amplitude: float, standard_deviation: float) -> np.ndarray:
    """
    Computes the normal distribution curve.

    Args:
        x (np.ndarray): Data array to evaluate the normal distribution on.
        mean (float): Mean of the distribution.
        amplitude (float): Peak amplitude of the normal curve.
        standard_deviation (float): Standard deviation of the distribution.

    Returns:
        np.ndarray: Evaluated normal curve over x.
    """
    return amplitude * np.exp( - (x - mean)**2 / (2*standard_deviation ** 2))


class ChiSquare:
    """
    Class to perform a Chi-Square statistical test on residual distributions.
    """

    def __init__(self, 
                 xmin : float,
                 xmax : float,
                 mean_window : int = 200, 
                 num_bins : int = 50,
                 model : Callable = normal) -> None:
        """
        Initializes the ChiSquare statistical test class.

        Args:
            xmin (float): Minimum value for the histogram range.
            xmax (float): Maximum value for the histogram range.
            mean_window (int): Number of trailing elements to use for mean calculation.
            num_bins (int): Number of bins for the histogram.
            model (Callable): The probability density model to fit against.
        """
        self.model = model
        self.xmin = xmin
        self.xmax = xmax
        self.num_bins = num_bins
        self.mean_window = mean_window


    def get_density(self, data: np.ndarray, xbins: int, xmin: float, xmax: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Calculates the density, frequencies, and bin edges for a given dataset.

        Args:
            data (np.ndarray): Input data array.
            xbins (int): Number of bins.
            xmin (float): Minimum range value.
            xmax (float): Maximum range value.

        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray]: Observed density, observed frequencies, and bin edges.
        """
        freq_obs, bin_edges = np.histogram(data, bins=xbins, range=(xmin,xmax), density=False)
        tot_obs             = len(data)
        bin_sizes           = np.diff(bin_edges)
        sum_freq            = np.sum(freq_obs)
        if sum_freq == 0:
            density_obs = np.zeros_like(freq_obs, dtype=float)
        else:
            density_obs = freq_obs / (sum_freq * bin_sizes)
        return density_obs, freq_obs, bin_edges
    

    def run(self, T: np.ndarray) -> Tuple[float, int, Dict[str, Any]]:
        """
        Runs the Chi-Square statistical test on the given temperature data array.

        Args:
            T (np.ndarray): Input temperature data array.

        Returns:
            Tuple[float, int, Dict[str, Any]]: Calculated chi2 value, degrees of freedom, and fit details.
        """
        degrees_of_freedom = self.num_bins - 1

        T_window = T[-self.mean_window:]
        T_mean = np.mean(T_window)
        T_residual = T_window - T_mean
        T_residual_std = np.std(T_residual)

        
        print(T_residual)
        print(T_mean)
        print(T_residual_std)

        density_obs, freq_obs, bin_edges = self.get_density(T_residual, xbins=self.num_bins, xmin=self.xmin, xmax=self.xmax)
        bin_centers      = bin_edges[:-1] + np.diff(bin_edges) / 2 
        bin_sizes        = np.diff(bin_edges) 
        prob_obs         = (density_obs*bin_sizes)


        # Chute inicial (p0) empiricamente muito bom a partir dos dados
        p0 = [0.0, max(density_obs) if max(density_obs) > 0 else 1.0, T_residual_std if T_residual_std > 0 else 1.0]
        try:
            params, _ = curve_fit(self.model, bin_centers, density_obs, p0=p0)
        except Exception:
            # Se o fit numérico falhar (ex: quando há zoom incorreto e quase todos os dados caem num único bin)
            # nós usamos a curva teórica ideal!
            params = p0
            
        x                  = np.linspace(bin_edges[0], bin_edges[-1], 10000)
        density_expected   = self.model(bin_centers, *params)

        density_expected_for_each_bin_center = self.model(bin_centers, *params) 
        prob_expected      = density_expected_for_each_bin_center * bin_sizes 
        freq_expected      = (prob_expected*len(T_residual)).astype(int)
        
        chi2 = 0
        for k in range(self.num_bins):
          if freq_expected[k] != 0:
            chi2+= ((freq_obs[k] - freq_expected[k])**2 / freq_expected[k])

        output = {'hist':{
                  'density_obs': density_obs,
                  'bin_edges'  : bin_edges,
                  'bin_centers': bin_centers,
                  'bin_sizes'  : bin_sizes,
                  'prob_obs'   : prob_obs,
                  'freq_obs'   : freq_obs,
                  },
            'fit':{
                  'x'               : x,
                  'density_expected': density_expected,
                  'params'          : params,
                  'density_expected_for_each_bin_center': density_expected_for_each_bin_center,
                  'prob_expected'   : prob_expected,
                  'freq_expected'   : freq_expected,
                  }
            }

        return chi2, degrees_of_freedom, output



    def plot_residuals(self, hist : Dict[str, Any], chi2: float, nbins: int, X: np.ndarray) -> None:
        """
        Plots the residuals comparing the observed density with the fitted model.

        Args:
            hist (Dict[str, Any]): Dictionary containing histogram and fit outputs from the run method.
            chi2 (float): Calculated chi2 value to display.
            nbins (int): Number of bins to display.
            X (np.ndarray): The residual array for mean/variance calculation.
        """
        density_obs      = hist['hist']['density_obs']
        bin_edges        = hist['hist']['bin_edges']
        bin_centers      = hist['hist']['bin_centers']
        bin_sizes        = hist['hist']['bin_sizes']
        x                = hist['fit']['x']
        params           = hist['fit']['params']
        density_expected = hist['fit']['density_expected']
        prob_expected    = hist['fit']['prob_expected']
        freq_expected    = hist['fit']['freq_expected']


        label = r'$f_x(x ,\mu = %.2f,\sigma = %.2f)$' % (params[0],params[2])
        plt.plot(x, normal(x, *params), label=label, color='red', linewidth=5)
        plt.stairs(density_obs, bin_edges, color='blue', label=r'$X$', linewidth=5)

        ytop        = 0.5
        mean        = np.mean(X)
        variance    = np.var(X)
        plt.axvline(mean, color='red', linestyle='dashed'  , linewidth=2, label=r'$\bar{X} = %.2f$'%mean)
        plt.axvline(mean - np.sqrt(variance), ymin=0, ymax=ytop, color='black', linestyle='dashed', linewidth=2, label=r'$\sqrt{s^2} \pm %1.2f$'%(np.sqrt(variance)) )
        plt.axvline(mean + np.sqrt(variance), ymin=0, ymax=ytop, color='black', linestyle='dashed', linewidth=2 )
        plt.text(bin_centers[-1]*0.6, ytop*0.8, r"$\chi^2=%1.2f$"%(chi2), fontsize=30 )
        plt.xlabel("x",  loc='right', fontsize=30)
        plt.ylabel(r"d(x)",  loc='top', fontsize=30  )
        plt.title(f"Densidade observada ($k_{{bins}}={nbins}$), $\chi^2={chi2:1.2f}$", fontsize=20)
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.show()

    def plot_chi2(self, chi2, degrees_of_freedom ):
        alpha = 0.05
        ymax=0.06
        
        x = np.linspace(0, 100, 500)
        pdf    = stats.chi2.pdf(x, degrees_of_freedom)
        # Create the plot
        plt.plot(x, pdf, label=r'$f_{\chi^2} (\chi_{o}^2, df=%i)$'%degrees_of_freedom, linewidth=5, color='blue')
        plt.plot(chi2, stats.chi2.pdf(chi2, degrees_of_freedom), "o" ,color='black', label=r'$\chi_{o}^2 = %1.2f$'%chi2, markersize=20)
        plt.axvline(x=chi2,ymin=0, ymax=stats.chi2.pdf(chi2, degrees_of_freedom)/ymax, linestyle='--', color='black', linewidth=3)
        plt.fill_between(x, pdf, where=x < chi2_critic, color='blue', alpha=0.2)
        plt.fill_between(x, pdf, where=x >= chi2_critic, color='red', alpha=0.5)
        plt.ylim([0, ymax])
        plt.xlim([0,100])
        plt.axvline(x=chi2_critic,ymin=0, ymax= stats.chi2.pdf(chi2_critic, degrees_of_freedom)/ymax, linestyle='--', color='red', label=r'$\chi_{crítico}^2(1-\alpha)=%1.2f$'%chi2_critic, linewidth=3)
        plt.title(r'Região de decisão ($\alpha = %1.2f$)'%(alpha), fontsize=30)
        plt.xlabel(r'$\chi_{o}^2$',loc='right', fontsize=30)
        plt.ylabel(r'$f_{\chi^2}(\chi_{o}^2)$',  loc='top', fontsize=30)
        plt.legend()
        plt.tight_layout()
        plt.show()