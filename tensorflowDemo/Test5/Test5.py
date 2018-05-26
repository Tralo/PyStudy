# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [0.199, 0.389, 0.589, 0.783, 0.980, 1.777, 1.380, 1.575, 1.771]
    A = np.vstack([x, np.ones(len(x))]).T
    a, b = np.linalg.lstsq(A, y)[0]
    x = np.array(x)
    y = np.array(y)
    plt.plot(x, y, 'o', label='Original data', markersize=10)
    plt.plot(x, a* x + b, 'r', label='Fitted line')
    plt.show()




