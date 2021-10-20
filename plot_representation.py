import numpy as np
import matplotlib.pyplot as plt


def context_plot(plotter):
    def wrapped(*args, **kwargs):
        plotter(*args)
        plt.xlabel("Budget")
        plt.ylabel("Quality")
        plt.title(kwargs["title"])
        plt.show()
        return None

    return wrapped


@context_plot
def plot_runs(runs):
    """
    Plot every runs on the same figure
    """
    for run in runs:
        costs, qualities = run
        plt.plot(costs, qualities)


@context_plot
def plot_eah(eah):
    plt.imshow(eah, cmap="Oranges", interpolation="nearest", origin="lower")


def plot_ert(ert, title="", x_label="Budget", y_label="Probability"):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(ert)
    plt.show()
