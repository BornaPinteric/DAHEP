import numpy as np
import scipy
import matplotlib.pyplot as plt
from pathlib import Path

#plot
gauss = lambda x, mean, dev: np.exp(-(x-mean)**2/2/dev)/np.sqrt(2*3.1415)/dev
x = np.arange(-10,10,0.1)
plt.figure(figsize=(8, 6))
plt.plot(x, np.array([gauss(i,0,1) for i in x]), label='mean=0, sigma=1')
plt.plot(x, np.array([gauss(i,0,3) for i in x]), label='mean=0, sigma=3')
plt.plot(x, np.array([gauss(i,3,3) for i in x]), label='mean=3, sigma=3')
plt.legend()
plt.title("Gaussian")
plt.tight_layout()
output_path = Path(__file__).resolve().parent / f"gaussian.png"
plt.savefig(output_path, dpi=300)

#integrali
print("---ZA MEAN=200GeV, SIGMA=2GeV---")
norm = scipy.stats.norm(loc=200,scale=2)
print("p( m>205Gev )=%.2f%%"%(100-100*norm.cdf(205)))
print("p( 199GeV<m<201Gev )=%.2f%%"%(100*norm.cdf(201)-100*norm.cdf(199)))
print("p( dvije m>203Gev )=%.2f%%"%(100*(1-norm.cdf(203))**2))