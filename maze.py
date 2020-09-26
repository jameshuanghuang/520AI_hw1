#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:32:35 2020
the maze
@author: jameshuang
"""
import numpy as np
import matplotlib.pyplot as plt

#use

class Maze:
    def __init__(self, rows, columns, prob_block):
        self.grid = np.random.choice(
                        a=[0, 1],
                        size=(rows, columns),
                        p=[1-prob_block,prob_block])
        self.grid[0][0] = 0
        self.grid[rows-1][columns-1] = 0
        self.rows = rows
        self.columns = columns
        self.prob_block = prob_block
        
    def print_maze(self):
        plt.imshow(self.grid, cmap='Greys',  interpolation='nearest')
        plt.show()

#m = Maze(10,10,0.3)
#m.print_maze()



