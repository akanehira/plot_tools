import pylab as pl
import numpy as np

def hinge(X):
    return np.maximum(1-X, 0)

def ramp(X):
    return np.minimum(hinge(X), 2)

def sigmoid(X):
    return 2.0 / (1 + np.exp(5*X))

def logistic(X):
    return np.log2(1 + np.exp(-X))

def zeroone(X):
    return map(lambda x : 0 if x>0 else 1, X)

def exp(X):
    return np.exp(-X)


def plot(mode):
    """ plot range """
    xmin, xmax, ymin, ymax = (-2, 2, -1, 3)
    fig = pl.figure()
    fig.subplots_adjust(left=0.15)
    ax = pl.subplot(1,1,1)

    interval = 0.5
    offset = 0.05

    """ move ticks"""
    pl.xticks(offset + np.arange(xmin, xmax+1, interval), np.arange(xmin, xmax+interval+1, interval))
    pl.yticks(offset + np.arange(ymin, ymax+1, interval), np.arange(ymin, ymax+interval+1, interval))

    pl.ylim([ymin,ymax])

    """ axis """
    pl.hlines([0], xmin, xmax, linestyles="dashed")
    pl.vlines([0], ymin, ymax, linestyles="dashed")

    """ label """
    pl.xlabel("x", style='italic', fontsize=25)
    pl.ylabel("l'(x)", style='italic', fontsize=25)

    """ title """
    pl.title(mode, fontdict={'size':28})

    X = np.linspace(xmin, xmax, 256, endpoint=True)

    """ plot funcitons """
    if mode == "(b)":
        pl.plot(X, exp(X), "--r", linewidth=5)
        pl.plot(X, hinge(X), "-b", linewidth=5)
    #pl.plot(X, logistic(X), linewidth=3, color="y")
    elif mode == "(a)":
        pl.plot(X, sigmoid(X), "-b", linewidth=5)
        pl.plot(X, ramp(X), "--r", linewidth=5)


    for i,item in enumerate(ax.get_xticklabels()):
        fontsize = 20
        item.set_fontsize(fontsize)

    for i,item in enumerate(ax.get_yticklabels()):
        fontsize = 20
        item.set_fontsize(fontsize)
    pl.show()


if __name__ == "__main__":
    for mode in ["(a)", "(b)"]:
        plot(mode)
