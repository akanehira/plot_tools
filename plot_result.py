# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

legent_dict = {"Sigmoid_weight": "Method 3 (proposed)",
               "SGDSVM_weight" : "Method 1",
               "Sigmoid": u"Method 2",
               "SGDSVM" : u"Baseline"}

def plot_res(mode, ax, color, marker, line, metric, l):
    fmt = marker + line + color
    res = np.loadtxt("./result/label%s/tmp/%s_%s_avg.txt"%(l, mode, metric)).T
    x = np.arange(0, 0.85, 0.10)
    y = np.mean(res, axis=0)
    #y=res[0, :] if len(res.shape) > 1 else res
    yerr1 = y - np.min(res, axis=0)
    yerr2 = np.max(res, axis=0) - y
    plt.plot(x, y, fmt,label = legent_dict[mode], ms=10, linewidth=3)
    ax.errorbar(x, y, yerr=[yerr1, yerr2], fmt=fmt, capsize=10, ms=10, elinewidth=3)

metrics = ["APsamples"]
min_max = { "APsamples" : (0.29, 0.39),
            }

def plots(l, legend):
    for metric in metrics:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        fig.subplots_adjust(left=0.15, bottom=0.15)
        #y_min, y_max = min_max[metric]
        #ax.set_ylim(y_min,y_max)

        for i, mode in enumerate([ "SGDSVM", "SGDSVM_weight", "Sigmoid","Sigmoid_weight"]):
            color = ["b", "r", "g", "k"][i]
            marker = ["o", "o", "s", "s"][i]
            line = ["-", "--", "-", "--"][i]

            plot_res(mode, ax, color, marker, line, metric, l)

        for i,item in enumerate(ax.get_xticklabels()):
            if i == len(ax.get_xticklabels())-1:
                fontsize = 0
            else:
                fontsize = 15
            item.set_fontsize(fontsize)

        for i,item in enumerate(ax.get_yticklabels()):
            if i == 0:
                fontsize = 0
            else:
                fontsize = 15
            item.set_fontsize(fontsize)

        if legend:
            plt.legend(loc='lower left', prop={'size':15})

        plt.title("mean number of label : %s"%l,  fontdict={'size':28})
        plt.xlabel("noise rate", fontsize=25)
        plt.ylabel(metric, fontsize=25)
        plt.savefig("./%s_label%s.png"%(metric, l))


for i, l in enumerate([3, 7, 15, 35]):
    if i==0:
        plots(l, True)
    else:
        plots(l, True)
