from scipy.stats import rv_discrete
import numpy as np

class SleepFin(rv_discrete):
    """
    A custom distribution class for generating sleep fin data.
    Inherits from scipy.stats.rv_discrete.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _argcheck(self, *args):
        return True

    def _pmf(self, k, mu):
        return np.exp(-k) * mu**k / np.math.factorial(k)  # PMF of the Poisson distribution

    def _cdf(self, x):
        return 1 - np.exp(-x)  # CDF of the exponential distribution
    

def main():
    # Example usage
    sleep_fin = SleepFin(name='sleep_fin')
    
    # Generate random samples
    samples = sleep_fin.rvs(size=1000)
    
    # Calculate PDF and CDF for a range of values
    x = np.linspace(0, 5, 100)
    pdf_values = sleep_fin.pmf(x)
    cdf_values = sleep_fin.cdf(x)

    print("Random Samples:", samples[:10])
    print("PDF Values:", pdf_values[:10])
    print("CDF Values:", cdf_values[:10])
    
    # Plotting the PDF and CDF
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(x, pdf_values, label='PDF', color='blue')
    plt.title('Probability Density Function')
    plt.xlabel('x')
    plt.ylabel('Density')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x, cdf_values, label='CDF', color='green')
    plt.title('Cumulative Distribution Function')
    plt.xlabel('x')
    plt.ylabel('Cumulative Probability')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()