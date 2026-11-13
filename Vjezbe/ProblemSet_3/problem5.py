import numpy as np
import scipy
import matplotlib.pyplot as plt
from pathlib import Path

def cdf(pdf, mini, x):
    return scipy.integrate.quad(pdf, mini, x)[0]

def find_min_x(func, mini, maks):
    a = mini
    b = maks
    while (b-a)>(maks-mini)/100:
        half = (b+a)/2
        interval = b-a
        left = half - 0.1*interval
        right = half + 0.1*interval
        if func(left) > func(right):
            a = left
        elif func(left) < func(right):
            b = right
        else:
            a = left
            b = right
    return (b+a)/2

def generate(pdf, mini, maks):
    u = np.random.uniform(0,1)
    return find_min_x(lambda t: abs(cdf(pdf, mini, t) - u), mini, maks)

#test
norm = scipy.stats.norm(scale=1)

x = np.arange(-5,5,0.1)
y = np.array([norm.pdf(i) for i in x])

N=1000
nums = np.zeros(N)
for i in range(N):
    nums[i] = generate(norm.pdf, -5, 5)

plt.figure(figsize=(8, 6))
plt.hist(nums, bins=20, histtype="step", linewidth=1.5, density=True)
plt.plot(x, y)
plt.ylabel("% of hits")
plt.title("histogram za norm pdf (inv method)")
plt.tight_layout()
output_path = Path(__file__).resolve().parent / f"inver.png"
plt.savefig(output_path, dpi=300)