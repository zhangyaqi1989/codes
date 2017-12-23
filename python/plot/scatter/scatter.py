import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Hello World")
    x = np.arange(100)
    y = np.random.rand(*x.shape)
    s = np.random.rand(*x.shape) * 800 + 500
    plt.scatter(x, y, s, c='g', alpha=0.5, marker='o')
    plt.show()
