# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import itertools
import os

class PlotMethods():
    def __init__(self, x_label, y_label, title, x_axis, save_dir="./", save_filename="img.jpg", xlim=None, ylim=None, legend_loc="lower left"):
        self.colors = [
            (0, 0.4470, 0.7410),
            (0.8500, 0.3250, 0.0980),
            (0.9290, 0.6940, 0.1250),
            (0.4940, 0.1840, 0.5560),
            (0.4660, 0.6740, 0.1880),
            (0.3010, 0.7450, 0.9330),
            (0.6350, 0.0780, 0.1840)
        ]
        self.markers = ["o", "s", "s", "o", ">", ">"]
        self.lines =  ["-", "--", "-", "--", "-", "--", "-", "--"]

        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.x_axis = x_axis
        self.save_dir = save_dir
        self.save_filename = save_filename
        self.legend_loc = legend_loc
        self.xlim, self.ylim = (xlim, ylim)

    def plot_graph(self, methods, results):
        """
        'methods' : list of string,
        each element corresponds to the name of method.
        'results' : numpy array (2d or 3d)
        the number of rows should be the same as the length of 'methods'
        """

        ax = self.init_figure()
        self.plot_res(ax, methods, results, is_errorbar=False)
        self.arange_graph()
        self.add_ticks(ax, is_x=True, is_y=True, size=18)
        self.save_fig(path=self.save_dir+self.save_filename)

    def plot_res(self, ax, methods, results, is_errorbar=False):
        for i, mode in enumerate(methods):
            plt.plot(self.x_axis, results[i, :], label=mode, ms=12, linewidth=4.5, marker=self.markers[i], color=self.colors[i], linestyle=self.lines[i])
            if is_errorbar:
                raise NotImplementedError("Not implemented.")
                yerr1 = y - y_min
                yerr2 = y_max - y
                ax.errorbar(self.x_axis, y, label=label, yerr=[yerr1, yerr2], capsize=10, ms=12,
                            linewidth=5, elinewidth=5, marker=marker, color=color, linestyle=line)

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
            plt.savefig(png_path, bbox_inches="tight", pad_inches=0.0)

    def arange_graph(self):
        """ arange graph """
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
    results = np.arange(27).reshape(3, 9) / 27.0
    p = PlotMethods("a", "b", "c")
    p.plot_graph(modes, results)
