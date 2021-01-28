"""
canvases.py -- Defines classes used for plotting and data visualization.
Copyright (C) 2021  Paul Sirri <paulsirri@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys
import matplotlib

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class InteractivePlot(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes_glucose = self.fig.add_subplot(111)
        self.axes_insulin = self.axes_glucose.twinx()
        self.axes_carb = None
        self.axes_exercise = None
        super(InteractivePlot, self).__init__(self.fig)


class BarGraph(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=3.8, height=.25):
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)
        super(BarGraph, self).__init__(fig)


class PieGraph(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(PieGraph, self).__init__(fig)
