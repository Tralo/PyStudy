# coding:utf-8
import matplotlib.pylab as plt
import numpy as np

if __name__ == '__main__':
    plt.subplot(2, 2, 3)
    n = 20
    Z = np.random.uniform(0, 1, n)
    plt.pie(Z)
    plt.subplot(2, 2, 4)
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    Y_C, Y_S = np.cos(X), np.sin(X)
    plt.plot(X, Y_C, color='blue', linewidth=2.5, linestyle='-')
    plt.plot(X, Y_S, color='red', linewidth=2.5, linestyle='-')


    plt.xlim(X.min()*1.1, X.max() * 1.1)
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi/2, np.pi],
               [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    plt.ylim(Y_C.min()*1.1, Y_C.max() * 1.1)
    plt.yticks([-1, 0, +1],
               [r'$-1$', r'$0$', r'$+1$'])
    plt.show()







