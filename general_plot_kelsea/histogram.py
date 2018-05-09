import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

def make_histogram(data, title, xlabel, ylabel):
    n, bins, patches = plt.hist(data, bins='auto')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def make_example_hist():

    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    n, bins, patches = plt.hist(x, 50, density=True, facecolor='green', alpha=0.75)

    y = mlab.normpdf(bins, mu, sigma)
    plt.plot(bins, y, 'r--', linewidth=1)

    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title("Just an example")
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)

    plt.show()