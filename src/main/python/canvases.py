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
        self.axes_carb_exercise = None
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
