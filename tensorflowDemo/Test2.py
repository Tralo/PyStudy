# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
# 双曲正切函数
if __name__ == '__main__':
    x = np.linspace(-100, 100, 1000)
    y = np.tanh(x)
    plt.plot(x, y, label="label", color="red", linewidth=1)
    plt.xlabel("abscissa")
    plt.ylabel("ordinate")
    plt.title("tanh Example")
    plt.show()
