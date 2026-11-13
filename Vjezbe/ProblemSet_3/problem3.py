import numpy as np
import scipy
import matplotlib.pyplot as plt
from pathlib import Path

def generate(pdf,mini,maks):
    global global_count
    x_sample = np.linspace(mini,maks,100)
    y_sample = np.array([pdf(i) for i in x_sample])
    y_max = 1.1*max(y_sample)
    while True:
        x_rand = np.random.uniform(mini,maks)
        y_rand = np.random.uniform(0,y_max)
        global_count+=1
        if y_rand < pdf(x_rand):
            return x_rand

global_count = 0

#test
norm = scipy.stats.norm(scale=1)

x = np.arange(-5,5,0.1)
y = np.array([norm.pdf(i) for i in x])

N=10000
nums = np.zeros(N)
for i in range(N):
    nums[i] = generate(norm.pdf, -5, 5)
print("Za %d brojeva generirani (x,y) unifrom par %d puta."%(N,global_count))

plt.figure(figsize=(8, 6))
plt.hist(nums, bins=20, histtype="step", linewidth=1.5, density=True)
plt.plot(x, y)
plt.ylabel("% of hits")
plt.title("histogram za norm pdf (acc/rej method)")
plt.tight_layout()
output_path = Path(__file__).resolve().parent / f"accrej.png"
plt.savefig(output_path, dpi=300)