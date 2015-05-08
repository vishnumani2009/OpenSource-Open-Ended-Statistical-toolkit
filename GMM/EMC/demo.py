
import csv
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from algorithm import EM
import argparse


def line_plot(data_arrays, xlabel, ylabel, labels, title, f):
    """
    Plots a scatter chart.
    Parameters
    ----------
    data_arrays: 2d numpy array
        Data to be plotted. This array consists of matrices of real values to be plotted.
        Each row of this matrix will be plotted as a line on the graph.
    xlabel: list of string
        The list of categories on for the x axis labels. The length of this list should be equal to the
        columns of the data_arrays.
    ylabel: string
        The label on the y axis.
    labels: list of string
        The labels for each category.
    title: string
        The title of the graph. Will be used as the name of the graph file.
    dest: string, optional
        Path to the directory to save the image
    Returns
    -------
    None:
        Saves the plot to the disk.
    """
    plt.suptitle(title, fontsize=14)
    plots = []
    for data in data_arrays:
        plot, = plt.plot(data)
        plots.append(plot)
    plt.legend(plots, labels, loc=2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(f, format="png")
    plt.show()
    plt.clf()

if __name__ == '__main__':
##    parser = argparse.ArgumentParser(description='Divides data into the categories by ')
##    parser.add_argument('data', type=argparse.FileType("rb"), help='CSV file of data input')
##    args = parser.parse_args()
##    # reading the file
##    with args.data as csvfile:
##        print type(csvfile)
    csvfile=open("input.csv","rb")
    reader = csv.reader(csvfile)
    input_list = np.array(map(lambda line: np.array(map(lambda i: float(i), line)), reader))

    x_list = input_list[:,0]
    #print x_list
    e_matrix = input_list[:,1:]
    #print e_matrix
    mean_matrix = EM.simulate_E_M(x_list, e_matrix, 100)
    line_plot(mean_matrix, 'step', 'mean', ['Distribution 1','Distribution 2','Distribution 3'], 'E-M Learning' ,'sample_result.png' )
