#!/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')


class LivePlotGui(object):
    pass

class LivePlotter(object):
    def __init__(self, title, nr_points=10, size=(13, 6), identifier='', pause_time=0.1):
        plt.ion()
        self.figure = None  # plt.figure(figsize=size)
        self.axis = None  # self.figure_.add_subplot(111)
        self.line = None
        self.title = title
        self.label = {'x': '',
                      'y': ''}
        self.y_data = np.linspace(0, 1, nr_points)[0:-1]
        self.x_data = np.linspace(-1, 0, nr_points)[0:-1]
        self.nr_points = nr_points

    def set_x_label(self, x_label):
        self.label['x'] = x_label

    def set_y_label(self, y_label):
        self.label['y'] = y_label

    def set_label(self, x_label, y_label):
        self.set_x_label(x_label)
        self.set_y_label(y_label)

    def _update_data(self, x, y):
        self.x_data = np.append(self.x_data, x)
        if len(self.x_data) > self.nr_points:
            self.x_data = np.delete(self.x_data,
                                    [i for i in range(len(self.x_data) - self.nr_points)])

        self.y_data = np.append(self.y_data, y)
        if len(self.y_data) + 1 >= self.nr_points:
            self.y_data = np.delete(self.y_data,
                                    [i for i in range(len(self.y_data) - self.nr_points)])

    def plot(self, x, y):
        self._update_data(x, y)
        if not self.line:
            plt.ion()
            self.figure = plt.figure(figsize=(13, 6))
            self.axis = self.figure.add_subplot(111)
            self.line, = self.axis.plot(self.x_data,
                                        self.y_data,
                                        '-o', alpha=0.8)

        self.line.set_ydata(self.y_data)
        plt.show()
#         self.axis.plot(self.x_data, self.y_data)
#        self.figure.show()

        # plt.ylabel(self.label['y'])
        # plt.title(self.title) # TODO: fix xtics!
#        plt.show(0)

    #         self.line.set_ydata(y)
    #         self._adjust_range()

    #         line1.set_ydata(y_data)
    #         # adjust limits if new data goes beyond bounds
    #         if np.min(y_data) <= line1.axes.get_ylim()[0] or np.max(y_data) >= line1.axes.get_ylim()[1]:
    #             plt.ylim([np.min(y_data) - np.std(y_data), np.max(y_data) + np.std(y_data)])
    #
    #         plt.xlim([x_vec[0], x_vec[-1]])
    #         # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    #         plt.pause(pause_time)
    #
    #         # return line so we can update it again in the next iteration
    #         return line1
    #         if not self.line_:
    #             plt.ion()

    def _adjust_range(self):
        self._adjust_range_x()
        self._adjust_range_y()

    def _adjust_range_x(self):
        x_min = np.min(self.x_data)
        x_min_plt = self.line.axes_get_xlim()[0]
        x_max = np.max(self.x_data)
        x_max_plt = self.line.axes_get_xlim()[1]
        if x_min <= x_min_plt or x_max >= x_max_plt:
            std = np.std(self.x_data)
            self.line.xlim([x_min - std, x_max + std])

    def _adjust_range_y(self):
        y_min = np.min(self.y_data)
        y_min_plt = self.line.axes_get_ylim()[0]
        y_max = np.max(self.y_data)
        y_max_plt = self.line.axes_get_ylim()[1]
        if y_min <= y_min_plt or y_max >= y_max_plt:
            std = np.std(self.y_data)
            self.line.ylim([y_min - std, y_max + std])


def live_plotter(x_vec, y_data, line1, identifier='', pause_time=0.1, title="title", y_label="y", x_label="x"):
    if not line1:
        plt.ion()
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)

        line1, = ax.plot(x_vec, y_data, '-o', alpha=0.8)

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(f'Title: {title}')
        # TODO: fix xtics!
        plt.show()

    line1.set_ydata(y_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y_data) <= line1.axes.get_ylim()[0] or np.max(y_data) >= line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y_data) - np.std(y_data), np.max(y_data) + np.std(y_data)])

#    plt.xlim([x_vec[0], x_vec[-1]])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)

    # return line so we can update it again in the next iteration
    return line1
