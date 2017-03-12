# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import itertools
import os

class PlotMethods():
    def __init__(self, x_label, y_label, title, save_dir="./",
                 save_filename="img.jpg", xlim=None, ylim=None,
                 is_errorbar=False, is_legend=False, legend_loc="lower left"
                 figsize=None):
        self.colors = [
            (0.8500, 0.3250, 0.0980),
            (0, 0.4470, 0.7410),
            (0.4940, 0.1840, 0.5560),
            (0.9290, 0.6940, 0.1250),
            (0.4660, 0.6740, 0.1880),
            (0.3010, 0.7450, 0.9330),
            (0.6350, 0.0780, 0.1840)
        ]
        self.markers = ["o", "s", "s", "o", ">", ">"]
        self.lines =  ["-", "--", "-", "--", "-", "--", "-", "--"]

        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.save_dir = save_dir
        self.save_filename = save_filename
        self.legend_loc = legend_loc
        self.is_errorbar = is_errorbar
        self.is_legend = is_legend
        self.xlim, self.ylim = (xlim, ylim)
        self.figsize = figsize

    def _check_mat_dim(self, mat):
        """
        if mat is array, return 2-d matrix
        """
        if mat.ndim == 1:
            return np.atleast_2d(mat)
        else:
            return mat

    def plot_graph(self, methods, x_axis, results, errors=None):
        """
        'methods' : list of string,
        each element corresponds to the name of method.
        'x_axis' : x-axis of the graph
        'results' : numpy array (2d or 3d)
        the number of rows should be the same as the length of 'methods'
        """

        results = self._check_mat_dim(results)
        if self.is_errorbar:
            errors = self._check_mat_dim(errors)
        ax = self.init_figure(figsize=self.figsize)
        self.plot_res(ax, methods, x_axis, results, errors)
        self.arange_graph()
        self.add_ticks(ax, is_x=True, is_y=True, size=18)
        self.save_fig(path=self.save_dir+self.save_filename)

    def plot_res(self, ax, methods, x_axis, results, errors):
        for i, mode in enumerate(methods):
            if self.is_errorbar:
                ax.errorbar(x_axis, results[i, :], label=mode,
                            yerr=[errors[i, :], errors[i, :]],
                            capsize=10, ms=12,linewidth=4.5,
                            elinewidth=4.5, marker=self.markers[i],
                            color=self.colors[i], linestyle=self.lines[i])
            else:
                plt.plot(x_axis, results[i, :],
                         label=mode, ms=12,
                         linewidth=4.5, marker=self.markers[i],
                         color=self.colors[i], linestyle=self.lines[i])


    def init_figure(self):
        """ initialize graph """
        fig = plt.figure()
        fig.subplots_adjust(left=0.15, bottom=0.15)
        ax = fig.add_subplot(111)
        return ax

    def save_fig(self, path):
        """ save both png and eps """
        if ".eps" in path:
            png_path = path.replace(".eps", ".png")
            plt.savefig(png_path, bbox_inches="tight", pad_inches=0.0)
            subprocess.call("convert %s %s"%(png_path, path), shell=True)
        else:
            png_path = path
            plt.savefig(png_path, bbox_inches="tight", pad_inches=0.0)

    def arange_graph(self):
        """ arange graph """
        if self.is_legend:
            lgd = plt.legend(loc=self.legend_loc, prop={'size':20})
        plt.title(self.title,  fontdict={'size':23})
        plt.grid(color='k', linestyle='--', linewidth=0.3)
        plt.xlabel(self.x_label, fontsize=25)
        plt.ylabel(self.y_label, fontsize=25)
        if self.xlim:
            plt.xlim(self.xlim)
        if self.ylim:
            plt.ylim(self.ylim)

    def add_ticks(self, ax, is_x=True, is_y=True, size=18):
        if is_x:
            for i, item in enumerate(ax.get_xticklabels()):
                if i == len(ax.get_xticklabels())-1:
                    fontsize = 0
                else:
                    fontsize = size
                item.set_fontsize(fontsize)

        if is_y:
            for i, item in enumerate(ax.get_yticklabels()):
                if i == 0:
                    fontsize = 0
                else:
                    fontsize = size
                item.set_fontsize(fontsize)

if __name__ == "__main__":
    """ how to use """
    modes = ["method", "method2", "method3"]
    x_axis = np.arange(0, 0.9, 0.1)
    print x_axis
    results = np.arange(27).reshape(3, 9) / 27.0
    p = PlotMethods("x_label", "y_label", "title of graph")
    p.plot_graph(modes, x_axis, results)
