#plote graphs for the data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def plot_time_series(data, column, title, xlabel, ylabel, label, color='blue', linewidth=2):
    """
    Plots a time series with customizable parameters.
    
    Args:
        data (DataFrame): The DataFrame containing the data.
        column (str): The column to plot.
        title (str): The title of the plot.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
        label (str): The label for the plot legend.
        color (str): Line color for the plot. Default is 'blue'.
        linewidth (int): Line width for the plot. Default is 2.
    """
    plt.figure(figsize=(15, 6))
    plt.plot(data.index, data[column], label=label, color=color, linewidth=linewidth)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.grid(alpha=0.3)
    plt.legend(fontsize=12)
    plt.show()
