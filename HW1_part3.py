# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:01:45 2020

@author: Pengfei Liu
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_sincostan():
    x=np.linspace(0,2*np.pi,100)
    sinx=np.sin(x)
    cosx=np.cos(x)
    tanx=np.tan(x)
    plt.grid()
    tanx[:-1][np.diff(tanx) < 0] = np.nan
    plt.plot(x,sinx,label='sin(x)')
    plt.plot(x,cosx,label='cos(x)')
    xmin, xmax, ymin, ymax =plt. axis()
    axes = plt.axes()
    axes.set_xlim([xmin, xmax])
    axes.set_ylim([ymin, ymax])
    plt.plot(x,tanx,label="tan(x)")
    plt.legend()
    plt.ylabel('y')
    plt.xlabel('x')
    plt.title('Sine Cosine and Tangent wave')
    plt.show()
if __name__ == '__main__':
    plot_sincostan()