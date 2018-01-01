import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    print("Hello World")
    cpus = np.loadtxt("cpu.txt")
    gpus = np.loadtxt("gpu.txt")
    ns = np.arange(1, 1 + len(cpus))
    plt.plot(ns, cpus, 'b-o', label="cpu")
    plt.plot(ns, gpus, 'r-s', label="gpu")
    plt.legend(loc="upper left")
    plt.show()

