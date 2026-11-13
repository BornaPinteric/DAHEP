import numpy as np
import scipy
import matplotlib.pyplot as plt
from pathlib import Path

#plot
norm = scipy.stats.norm()
x = np.arange(-5,5,0.1)
plt.figure(figsize=(8, 6))
plt.plot(x, np.zeros(len(x)), 'k--')
plt.plot(x, np.ones(len(x)), 'k--')
plt.plot(x, norm.cdf(x))
plt.title("CDF (mean=0, sigma=1)")
plt.tight_layout()
output_path = Path(__file__).resolve().parent / f"cdf.png"
plt.savefig(output_path, dpi=300)