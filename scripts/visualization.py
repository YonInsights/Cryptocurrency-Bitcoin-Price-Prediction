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

def plot_time_series_with_moving_averages(data, column, ma_columns, ma_styles, title, xlabel, ylabel, label, color='blue', linewidth=2):
    """
    Plots a time series with additional moving averages.
    
    Args:
        data (DataFrame): The DataFrame containing the data.
        column (str): The column to plot as the main time series.
        ma_columns (list): List of moving average columns to plot.
        ma_styles (list): List of dictionaries defining the styles for each moving average line.
                          Example: [{'color': 'green', 'linestyle': '-'}, {'color': 'red', 'linestyle': '--'}]
        title (str): The title of the plot.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
        label (str): The label for the main plot legend.
        color (str): Line color for the main plot. Default is 'blue'.
        linewidth (int): Line width for the main plot. Default is 2.
    """
    plt.figure(figsize=(15, 6))
    # Plot the main time series
    plt.plot(data.index, data[column], label=label, color=color, linewidth=linewidth)
    
    # Plot each moving average with its style
    for ma_col, style in zip(ma_columns, ma_styles):
        plt.plot(data.index, data[ma_col], label=ma_col, color=style['color'], linestyle=style['linestyle'], linewidth=linewidth)
    
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.grid(alpha=0.3)
    plt.legend(fontsize=12)
    plt.show()
def plot_predictions(plotting_data):
    plt.figure(figsize=(15, 6))
    plt.plot(plotting_data.index, plotting_data['Original'], label='Original', color='blue', linewidth=2)
    plt.plot(plotting_data.index, plotting_data['Prediction'], label='Prediction', color='red', linewidth=2)
    plt.title("Prediction vs Actual Close Price", fontsize=14)
    plt.ylabel('Close Price', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.grid(alpha=0.3)
    plt.legend(fontsize=14)
    plt.show()





