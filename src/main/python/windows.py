import os
import csv
from datetime import datetime, timedelta
import numpy as np
import copy
import pandas as pd

from PyQt5.QtCore import QDateTime, QTime, QDate
# import time
import calendar

# from PyQt5.QtGui import QImage, QPixmap, QGuiApplication
# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QCheckBox
# QAbstractItemView, QTableWidget, QTableWidgetItem, QDialog, QProgressBar,
# QPushButton, QApplication, QTabWidget, QWidget, QVBoxLayout, QLabel

# import matplotlib
# matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
#     NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure
from matplotlib.markers import MarkerStyle

from ui.glucokeep_startscreen_v1 import Ui_MainWindow as Start_Ui
from ui.glucokeep_event_selector_v5 import Ui_MainWindow as Selection_Ui
from ui.glucokeep_eventglucose_v5 import Ui_MainWindow as Glucose_Ui
from ui.glucokeep_eventcarbs_v5 import Ui_MainWindow as Carbs_Ui
from ui.glucokeep_eventexercise_v5 import Ui_MainWindow as Exercise_Ui
from ui.glucokeep_event_insulinfast_v5 import Ui_MainWindow as FastInsulin_Ui
from ui.glucokeep_event_insulinlong_v5 import Ui_MainWindow as LongInsulin_Ui
from ui.glucokeep_visualizer_v1 import Ui_MainWindow as Visualizer_Ui

import sys
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.ticker as ticker

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from metrics import get_time_in_range, interpolate_glucose, group_events_by_hour_in_day, \
    group_glucose_by_hour_in_day, get_iqr, group_interp_glucose_by_hour_in_day
import matplotlib.cbook as cbook

import matplotlib.colors
import matplotlib.gridspec as gridspec
import colorsys


# formats for datetime:
# datetime.strptime(string, '%m/%d/%Y %I:%M %p')
# datetime.strftime(datetime, '%m/%d/%y %I:%M %p')


class StartWindow(QMainWindow, Start_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super(StartWindow, self).__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("GlucoKeep  Start")

        # instantiate menu options
        self.selection_window = None
        self.visualizer_window = None

        # connect UI elements using slots and signals
        self.btn_addevent.clicked.connect(self.add_event)
        self.btn_visualize.clicked.connect(self.visualize)
        # TODO: last button

    def add_event(self):
        self.selection_window = SelectionWindow(self.ctx)
        self.selection_window.show()
        # self.hide()

    def visualize(self):
        path_to_file = self.choose_file()
        if path_to_file:
            self.visualizer_window = VisualizerWindow(self.ctx, path_to_file)
            self.visualizer_window.show()
            self.hide()
        else:
            print('\nno file was found\n')

    def choose_file(self):
        path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            return path


class SelectionWindow(QMainWindow, Selection_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super(SelectionWindow, self).__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("Add Event")

        # connect UI elements using slots and signals
        self.glucose_button.clicked.connect(self.glucose_event)
        self.carbs_button.clicked.connect(self.carbs_event)
        self.exercise_button.clicked.connect(self.exercise_event)
        self.insfast_button.clicked.connect(self.fast_insulin_event)
        self.pushButton_2.clicked.connect(self.long_insulin_event)
        self.cancel_btn.clicked.connect(self.cancel_event)

    def glucose_event(self):
        self.glucose_window = GlucoseWindow(self.ctx)
        self.glucose_window.show()
        self.hide()

    def carbs_event(self):
        self.carbs_window = CarbsWindow(self.ctx)
        self.carbs_window.show()
        self.hide()

    def exercise_event(self):
        self.exercise_window = ExerciseWindow(self.ctx)
        self.exercise_window.show()
        self.hide()

    def fast_insulin_event(self):
        self.fast_insulin_window = FastInsulinWindow(self.ctx)
        self.fast_insulin_window.show()
        self.hide()

    def long_insulin_event(self):
        self.long_insulin_window = LongInsulinWindow(self.ctx)
        self.long_insulin_window.show()
        self.hide()

    def cancel_event(self):
        self.close()


class GlucoseWindow(QMainWindow, Glucose_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super(GlucoseWindow, self).__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("Glucose Event")

        # set current time
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # connect UI elements using slots and signals
        self.save_btn.clicked.connect(self.save_event)
        self.cancel_btn.clicked.connect(self.cancel_event)

    def save_event(self):
        dt = self.dateTimeEdit.dateTime().toString("MM/dd/yyyy HH:mm AP")
        category = 0
        value_one = self.spinbox_bg.value()
        value_two = None
        event = [dt, category, value_one, value_two]
        if self.append_to_csv(event):
            self.close()

    def cancel_event(self):
        self.close()

    def append_to_csv(self, new_event):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            # open for writing, appending to the end of the file if it exists
            with open(path[0], 'a+') as csv_file:
                writer = csv.writer(csv_file)
                # add event as last row in the csv file
                writer.writerow(new_event)
                return True


class CarbsWindow(QMainWindow, Carbs_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super(CarbsWindow, self).__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("Carbs Event")

        # set current time
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # connect UI elements using slots and signals
        self.save_btn.clicked.connect(self.save_event)
        self.cancel_btn.clicked.connect(self.cancel_event)

    def save_event(self):
        dt = self.dateTimeEdit.dateTime().toString("MM/dd/yyyy HH:mm AP")
        category = 1
        value_one = self.spinbox_carbs.value()
        value_two = None
        event = [dt, category, value_one, value_two]
        self.append_to_csv(event)
        self.close()

    def cancel_event(self):
        self.close()

    def append_to_csv(self, new_event):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            # open for writing, appending to the end of the file if it exists
            with open(path[0], 'a+') as csv_file:
                writer = csv.writer(csv_file)
                # add event as last row in the csv file
                writer.writerow(new_event)


class ExerciseWindow(QMainWindow, Exercise_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super(ExerciseWindow, self).__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("Exercise Event")

        # set current time
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # connect UI elements using slots and signals
        self.save_btn.clicked.connect(self.save_event)
        self.cancel_btn.clicked.connect(self.cancel_event)

    def save_event(self):
        dt = self.dateTimeEdit.dateTime().toString("MM/dd/yyyy HH:mm AP")
        category = 2
        value_one = self.spinbox_duration.value()
        value_two = self.listwidget.currentRow()
        event = [dt, category, value_one, value_two]
        self.append_to_csv(event)
        self.close()

    def cancel_event(self):
        self.close()

    def append_to_csv(self, new_event):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            # open for writing, appending to the end of the file if it exists
            with open(path[0], 'a+') as csv_file:
                writer = csv.writer(csv_file)
                # add event as last row in the csv file
                writer.writerow(new_event)


class FastInsulinWindow(QMainWindow, FastInsulin_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super(FastInsulinWindow, self).__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("Fast-Acting Insulin Event")

        # set current time
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # connect UI elements using slots and signals
        self.save_btn.clicked.connect(self.save_event)
        self.cancel_btn.clicked.connect(self.cancel_event)

    def save_event(self):
        dt = self.dateTimeEdit.dateTime().toString("MM/dd/yyyy HH:mm AP")
        category = 3
        value_one = round(self.spinbox_units.value(), 2)
        value_two = None
        event = [dt, category, value_one, value_two]
        self.append_to_csv(event)
        self.close()

    def cancel_event(self):
        self.close()

    def append_to_csv(self, new_event):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            # open for writing, appending to the end of the file if it exists
            with open(path[0], 'a+') as csv_file:
                writer = csv.writer(csv_file)
                # add event as last row in the csv file
                writer.writerow(new_event)


class LongInsulinWindow(QMainWindow, LongInsulin_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super(LongInsulinWindow, self).__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("Long-Acting Insulin Event")

        # set current time
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # connect UI elements using slots and signals
        self.save_btn.clicked.connect(self.save_event)
        self.cancel_btn.clicked.connect(self.cancel_event)

    def save_event(self):
        dt = self.dateTimeEdit.dateTime().toString("MM/dd/yyyy HH:mm AP")
        category = 4
        value_one = round(self.spinbox_units.value(), 2)
        value_two = None
        event = [dt, category, value_one, value_two]
        self.append_to_csv(event)
        self.close()

    def cancel_event(self):
        self.close()

    def append_to_csv(self, new_event):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            # open for writing, appending to the end of the file if it exists
            with open(path[0], 'a+') as csv_file:
                writer = csv.writer(csv_file)
                # add event as last row in the csv file
                writer.writerow(new_event)


def adjust_lightness(color, amount=0.5):
    """ A static function that adjusts the brightness of a color in Matplotlib.
    https://stackoverflow.com/questions/37765197/darken-or-lighten-a-color-in-matplotlib """
    try:
        c = matplotlib.colors.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*matplotlib.colors.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], max(0, min(1, amount * c[1])), c[2])


def timedelta_to_string(seconds):
    # days
    days = seconds // 86400
    # remaining seconds
    seconds = seconds - (days * 86400)
    # hours
    hours = seconds // 3600
    # remaining seconds
    seconds = seconds - (hours * 3600)
    # minutes
    minutes = seconds // 60
    # remaining seconds
    seconds = seconds - (minutes * 60)
    return int(days), int(hours)


class VisualizerWindow(QMainWindow, Visualizer_Ui):
    def __init__(self, ctx, path_to_file, *args, **kwargs):
        super(VisualizerWindow, self).__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("GlucoKeep  Visualize Data")

        # set set widgets to expand
        self.mainplot.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                    QtWidgets.QSizePolicy.Expanding)

        # connect signals and slots
        self.setup_signals_and_slots()

        # read data from csv file, format as list of event records
        self.all_events = self.read_csv(path=path_to_file)

        # set initial values for basic interface parameters
        self.setup_initial_parameters()

        # initialize variables
        self.events = None
        self.events_t = None
        self.time_series = None
        self.event_types = None
        self.values = None
        self.exercise_intensities = None
        self.events_glucose = None
        self.events_glucose_t = None
        self.events_carb = None
        self.events_exercise = None
        self.events_insulin_fast = None
        self.events_insulin_long = None
        self.glucose_grouped_by_hour_in_day = None
        self.interp_glucose_grouped_by_hour_in_day = None

        # define color scheme for data visualization widgets
        self.color_stack = [adjust_lightness('r', 0.75),
                            'r',
                            adjust_lightness('limegreen', 0.9),
                            adjust_lightness('gold', 1.2),
                            adjust_lightness('gold', 0.85)]

        # load the window
        self.refresh_all()

    ##############################
    # METHODS TO RECEIVE SIGNALS
    ##############################

    def refresh_all(self):
        """ A method to refresh visual components of window based on user inputs. """

        print('\nrefresh_all()')

        if self.event_carb.isChecked() and self.event_exercise.isChecked():
            self.mainplot.fig.clf()
            grid = gridspec.GridSpec(ncols=1, nrows=2, figure=self.mainplot.fig,
                                     height_ratios=[4, 1])
            self.mainplot.axes_glucose = self.mainplot.fig.add_subplot(grid[0, 0])
            self.mainplot.axes_insulin = self.mainplot.axes_glucose.twinx()
            self.mainplot.axes_carb = self.mainplot.fig.add_subplot(grid[1, 0])
            self.mainplot.axes_exercise = self.mainplot.axes_carb.twinx()
        elif self.event_carb.isChecked():
            self.mainplot.fig.clf()
            grid = gridspec.GridSpec(ncols=1, nrows=2, figure=self.mainplot.fig,
                                     height_ratios=[4, 1])
            self.mainplot.axes_glucose = self.mainplot.fig.add_subplot(grid[0, 0])
            self.mainplot.axes_insulin = self.mainplot.axes_glucose.twinx()
            self.mainplot.axes_carb = self.mainplot.fig.add_subplot(grid[1, 0])
        elif self.event_carb.isChecked():
            self.mainplot.fig.clf()
            grid = gridspec.GridSpec(ncols=1, nrows=2, figure=self.mainplot.fig,
                                     height_ratios=[4, 1])
            self.mainplot.axes_glucose = self.mainplot.fig.add_subplot(grid[0, 0])
            self.mainplot.axes_insulin = self.mainplot.axes_glucose.twinx()
            self.mainplot.axes_carb = self.mainplot.fig.add_subplot(grid[1, 0])
        else:
            self.mainplot.fig.clf()
            self.mainplot.axes_glucose = self.mainplot.fig.add_subplot(111)
            self.mainplot.axes_insulin = self.mainplot.axes_glucose.twinx()
            self.mainplot.axes_carb = None

        # clear all plots
        self.mainplot.axes_glucose.cla()
        self.mainplot.axes_insulin.cla()
        if self.mainplot.axes_carb:
            self.mainplot.axes_carb.cla()
        self.tir_bargraph.axes.cla()
        self.tir_piegraph.axes.cla()
        self.avggluc_bargraph.axes.cla()
        self.stdv_bargraph.axes.cla()

        ####################################################
        # ONLY USE DATA IN CURRENT USER-DEFINED TIME RANGE
        ####################################################

        # TODO: only use data in user-defined time range

        # get the user-defined time range from QDateTimeEdit widgets
        time_a = self.time_a.dateTime().toPyDateTime()
        time_b = self.time_b.dateTime().toPyDateTime()
        self.update_duration_label()

        # use the requested time range to access a subset of the data from CSV file
        self.events = [event for event in self.all_events if
                       (event[0] <= time_b) and (event[0] >= time_a)]

        ###################################
        # UNPACK DATA FOR EACH EVENT TYPE
        ###################################

        # TODO: read dataset to object-oriented events

        # subset of data containing events that pertain only to blood glucose measurements
        self.events_glucose = [[event[0], event[2]] for event in self.events if event[1] is 0]

        # subset of data containing events that pertain only to carbs
        self.events_carb = [[event[0], event[2]] for event in self.events if event[1] is 1]

        # subset of data containing events that pertain only to exercise
        self.events_exercise = [[event[0], event[2]] for event in self.events if event[1] is 2]

        # subset of data containing events that pertain only to fast-acting insulin doses
        self.events_insulin_fast = [[event[0], event[2]] for event in self.events if event[1] is 3]

        # subset of data containing events that pertain only to long-acting insulin doses
        self.events_insulin_long = [[event[0], event[2]] for event in self.events if event[1] is 4]

        # transpose the data to allow convenient access to columns
        self.events_glucose_t = list(zip(*self.events_glucose))

        # group all glucose measurement events by the hour-of-day (0-23)
        self.glucose_grouped_by_hour_in_day = group_glucose_by_hour_in_day(self.events)

        # interpolated glucose levels in the time range
        glucose_interpolated, time_interpolated = interpolate_glucose(self.events_glucose)

        # group all glucose measurement events by the hour-of-day (0-23)
        self.interp_glucose_grouped_by_hour_in_day = group_interp_glucose_by_hour_in_day(
            glucose_interpolated, time_interpolated)

        ###########################################################################################
        #                                     PLOTTING
        ###########################################################################################

        # set color zones on the main plot's background
        self.mainplot.axes_glucose.axhspan(70, 180, color='limegreen', alpha=0.1)
        # self.mainplot.axes_glucose.axhspan(0, 70, color='red', alpha=0.1)
        # self.mainplot.axes_glucose.axhspan(180, 800, color='yellow', alpha=0.1)

        self.mainplot.axes_glucose.axhline(69, color='red', lw=3, alpha=0.7)
        self.mainplot.axes_glucose.axhline(181, color=adjust_lightness('gold', 1.2), lw=3)

        if not self.toggle_median.isChecked():
            medianprops = dict(linewidth=0)
        else:
            medianprops = None

        show_insulin_axis = False

        if self.toggle_iqr_all.isChecked():
            stats = get_iqr(self.interp_glucose_grouped_by_hour_in_day, q1=0, q3=100)
            self.mainplot.axes_glucose.bxp([stat for stat in stats.values()],
                                           positions=np.linspace(0.5, 23.5, 24),
                                           widths=[1 for stat in stats],
                                           flierprops=dict(linewidth=0),
                                           capprops=dict(linewidth=0),
                                           whiskerprops=dict(linewidth=0),
                                           medianprops=medianprops,
                                           boxprops=dict(alpha=0.4),
                                           showcaps=False,
                                           showfliers=False,
                                           showmeans=False,
                                           zorder=1)
        if self.toggle_iqr_eighty.isChecked():
            stats = get_iqr(self.interp_glucose_grouped_by_hour_in_day, q1=10, q3=90)
            self.mainplot.axes_glucose.bxp([stat for stat in stats.values()],
                                           positions=np.linspace(0.5, 23.5, 24),
                                           widths=[1 for stat in stats],
                                           flierprops=dict(linewidth=0),
                                           capprops=dict(linewidth=0),
                                           whiskerprops=dict(linewidth=0),
                                           medianprops=medianprops,
                                           boxprops=dict(alpha=0.4),
                                           showcaps=False,
                                           showfliers=False,
                                           showmeans=False,
                                           zorder=2)
        if self.toggle_iqr_fifty.isChecked():
            stats = get_iqr(self.interp_glucose_grouped_by_hour_in_day, q1=25, q3=75)
            self.mainplot.axes_glucose.bxp([stat for stat in stats.values()],
                                           positions=np.linspace(0.5, 23.5, 24),
                                           widths=[1 for stat in stats],
                                           flierprops=dict(linewidth=0),
                                           capprops=dict(linewidth=0),
                                           whiskerprops=dict(linewidth=0),
                                           medianprops=medianprops,
                                           boxprops=dict(alpha=0.4),
                                           showcaps=False,
                                           showfliers=False,
                                           showmeans=False,
                                           zorder=3)
        if self.toggle_median.isChecked() and not self.toggle_iqr_all.isChecked():
            # when only the median is show, but not dispersion box plots
            if not self.toggle_iqr_eighty.isChecked() and not self.toggle_iqr_fifty.isChecked():
                stats = get_iqr(self.interp_glucose_grouped_by_hour_in_day, q1=0, q3=100)
                self.mainplot.axes_glucose.bxp([stat for stat in stats.values()],
                                               positions=np.linspace(0.5, 23.5, 24),
                                               widths=[1 for stat in stats],
                                               flierprops=dict(linewidth=0),
                                               capprops=dict(linewidth=0),
                                               whiskerprops=dict(linewidth=0),
                                               medianprops=medianprops,
                                               boxprops=dict(alpha=0.3),
                                               showcaps=False,
                                               showfliers=False,
                                               showmeans=False,
                                               showbox=False,
                                               zorder=4)
        if self.event_bg.isChecked():
            x_data = [round(int(event[0].hour) + (int(event[0].minute) / 60), 2) for event in
                      self.events_glucose]
            y_data = [event[1] for event in self.events_glucose]
            self.mainplot.axes_glucose.scatter(x_data, y_data,
                                               s=1.5,
                                               c='blue',
                                               zorder=20,
                                               label='Glucose Reading')
        if self.event_carb.isChecked():
            x_data = [round(int(event[0].hour) + (int(event[0].minute) / 60), 2) for event in
                      self.events_carb]
            y_data = [event[1] for event in self.events_carb]

            # TODO: create a secondary subplot
            """grid = gridspec.GridSpec(ncols=1, nrows=2, figure=self.mainplot.fig,
                                     height_ratios=[4, 1],
                                     hspace=0.2)
            self.mainplot.axes_glucose = self.mainplot.fig.add_subplot(grid[0, 0])
            # self.mainplot.axes_insulin = self.mainplot.fig.add_subplot(grid[0, 0])
            self.mainplot.axes_carb = self.mainplot.fig.add_subplot(grid[1, 0])

            # self.mainplot.fig.subplots_adjust(bottom=0.3, top=0.95)
            # self.mainplot.axes_carb = self.mainplot.fig.add_subplot(212)"""

            #########################

            self.mainplot.axes_carb.scatter(x_data, y_data,
                                                     s=11,
                                                     c='darkorange',
                                                     zorder=10,
                                                     marker='D',
                                                     label='Carbs')
            # self.mainplot.axes_carb.get_yaxis().set_visible(False)
            # self.mainplot.axes_carb.get_xaxis().set_visible(False)

            # box = self.mainplot.axes_carb.get_position()
            # box.x0 = box.x0 + 0.2
            # box.x1 = box.x1 + 0.01
            # self.mainplot.axes_carb.set_position(box)

        if self.event_exercise.isChecked():
            x_data = [round(int(event[0].hour) + (int(event[0].minute) / 60), 2) for event in
                      self.events_exercise]
            y_data = [event[1] for event in self.events_exercise]
            self.mainplot.axes_carb.scatter(x_data, y_data,
                                               s=15,
                                               c='cyan',
                                               zorder=11,
                                               marker='+',
                                               label='Exercise')
        if self.event_insfast.isChecked():
            x_data = [round(int(event[0].hour) + (int(event[0].minute) / 60), 2) for event in
                      self.events_insulin_fast if event[1] < 50]
            y_data = [event[1] for event in self.events_insulin_fast if event[1] < 50]
            show_insulin_axis = True
            self.mainplot.axes_insulin.scatter(x_data, y_data,
                                               s=11,
                                               c='lime',
                                               zorder=13,
                                               marker='^',
                                               alpha=0.6,
                                               label='Fast-Acting Insulin Dose')
        if self.event_inslong.isChecked():
            x_data = [round(int(event[0].hour) + (int(event[0].minute) / 60), 2) for event in
                      self.events_insulin_long if event[1] < 50]
            y_data = [event[1] for event in self.events_insulin_long if event[1] < 50]
            show_insulin_axis = True
            self.mainplot.axes_insulin.scatter(x_data, y_data,
                                               s=11,
                                               c='magenta',
                                               zorder=12,
                                               marker='s',
                                               alpha=0.6,
                                               label='Long-Acting Insulin Dose')

        #################
        # PLOTTING 2
        #################

        # TODO: ALL DATA VIEW (separate tab)
        # clear all plots
        # self.mainplot.axes_glucose.cla()
        # self.tir_bargraph.axes.cla()

        # scatter plot of all glucose measurements in time range chronologically
        # self.mainplot.axes_glucose.scatter(self.events_glucose_t[0], self.events_glucose_t[1], c='blue', s=0.5)

        # line plot of interpolated glucose levels in time range chronologically
        # glucose_interpolated, time_interpolated = interpolate_glucose(self.events_glucose)
        # self.mainplot.axes_glucose.plot(time_interpolated, glucose_interpolated, c='red', lw=0.75)

        ########################
        # FORMAT THE MAIN PLOT
        ########################

        # format x-axis text
        labels = ['12AM', '3AM', '6AM', '9AM', '12PM', '3PM', '6PM', '9PM', '12AM']
        self.mainplot.axes_glucose.set_xticks(range(0, 25, 3))
        self.mainplot.axes_glucose.set_xticklabels(labels)

        # format glucose y-axis text
        max_glucose = max([ev[1] for ev in self.events_glucose])
        self.mainplot.axes_glucose.set_yticks(range(0, 401, 25))

        # format insulin y-axis text
        self.mainplot.axes_insulin.set_yticks(range(0, 51, 5))
        self.mainplot.axes_insulin.get_yaxis().set_visible(show_insulin_axis)

        # format figure
        self.mainplot.axes_glucose.set_zorder(1)
        self.mainplot.axes_glucose.patch.set_visible(False)
        self.mainplot.axes_glucose.grid(True, alpha=0.25)

        # axis labels
        self.mainplot.axes_glucose.set_ylabel('Blood Glucose (mg/dL)')
        self.mainplot.axes_glucose.set_xlabel('Hour of Day')
        self.mainplot.axes_glucose.set_title('Daily Trends of Blood Glucose')

        handles_glucose, labels_glucose = self.mainplot.axes_glucose.get_legend_handles_labels()
        handles_insulin, labels_insulin = self.mainplot.axes_insulin.get_legend_handles_labels()
        handles = handles_glucose + handles_insulin
        labels_legend = labels_glucose + labels_insulin
        self.mainplot.axes_glucose.legend(handles, labels_legend, loc='upper left')
        # labels=['Blood Glucose (mg/dL)']

        ##################################
        # TODO: FORMAT THE CARBS/EXERCISE PLOT
        ##################################

        """# format x-axis text
        labels = []
        self.mainplot.axes_glucose.set_xticks(range(0, 25, 3))
        self.mainplot.axes_glucose.set_xticklabels(labels)

        # format glucose y-axis text
        self.mainplot.axes_glucose.set_yticks(range(0, 126, 25))

        # format insulin y-axis text
        self.mainplot.axes_insulin.set_yticks(range(0, 51, 5))
        self.mainplot.axes_insulin.get_yaxis().set_visible(show_insulin_axis)

        # format figure
        self.mainplot.axes_glucose.set_zorder(1)
        self.mainplot.axes_glucose.patch.set_visible(False)
        self.mainplot.axes_glucose.grid(True, alpha=0.25)

        # axis labels
        self.mainplot.axes_glucose.set_ylabel('Blood Glucose (mg/dL)')
        self.mainplot.axes_glucose.set_xlabel('Hour of Day')
        self.mainplot.axes_glucose.set_title('Daily Trends of Blood Glucose')

        handles_glucose, labels_glucose = self.mainplot.axes_glucose.get_legend_handles_labels()
        handles_insulin, labels_insulin = self.mainplot.axes_insulin.get_legend_handles_labels()
        handles = handles_glucose + handles_insulin
        labels_legend = labels_glucose + labels_insulin
        self.mainplot.axes_glucose.legend(handles, labels_legend, loc='upper left')"""
        # labels=['Blood Glucose (mg/dL)']

        ##########################
        # UPDATING OTHER WIDGETS
        ##########################

        #################
        # TIME IN RANGE
        #################

        # Time in Range (horizontal bar graph using interpolated data)
        time_in_range = get_time_in_range(glucose_interpolated)
        labels = ['>250 mg/dL', '180-250 mg/dL', '70-180 mg/dL', '54-70 mg/dL', '<54 mg/dL']

        self.tir_bargraph.axes.barh(labels, time_in_range.values(),
                                    color=list(reversed(self.color_stack)))

        for index, value in enumerate(list(time_in_range.values())):
            self.tir_bargraph.axes.text(95, index + 0.2, str(round(value, 1)) + '%', ha='right')
        self.tir_bargraph.axes.set_xlim(0, 100)
        self.tir_bargraph.axes.invert_yaxis()
        self.tir_bargraph.setMinimumSize(1, 200)
        self.tir_bargraph.axes.get_yaxis().set_visible(False)
        # self.tir_bargraph.axes.get_xaxis().set_visible(False)
        # self.tir_bargraph.pie = self.tir_bargraph.add_subplot(112)
        self.tir_bargraph.axes.xaxis.set_ticks(ticks=range(0, 101, 25))

        # Time in Range (pie graph using interpolated data)
        self.tir_piegraph.setMinimumSize(1, 200)
        # self.verticalLayout_8.removeWidget(self.tir_piegraph)
        self.tir_piegraph.axes.pie(time_in_range.values(),
                                   # labels=labels,
                                   colors=list(reversed(self.color_stack)),
                                   center=(0, 100)
                                   # wedgeprops={'linewidth': 1}
                                   # autopct='%1.1f%%',
                                   # shadow=True,
                                   # startangle=90
                                   )

        # self.tir_piegraph.axes.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        #######################################
        # TODO: FORMAT LEGEND FOR RIGHT-HAND COLUMN
        #######################################

        self.tir_piegraph.axes.legend(bbox_to_anchor=(-1.1, 1), loc='upper left',
                                      borderaxespad=0., labels=labels)

        ##########################
        # AVERAGE DAILY READINGS
        ##########################

        # Average Number of Daily Readings
        count = len(self.events_glucose)
        days = int((time_b - time_a).days)
        if days < 1:
            # less than a day is still a day, cannot divide by zero
            days = 1
        average_num_glucose_msmts = round(count / days, 1)
        self.dayreadings.setText(str(average_num_glucose_msmts))

        # Average Glucose
        average_glucose = round(np.average([event[1] for event in self.events_glucose]))
        self.avggluc.setText(str(average_glucose) + ' mg/dL')
        # color bar plot
        self.setup_slider_graph(self.avggluc_bargraph)
        self.avggluc_bargraph.axes.scatter([average_glucose], [1], marker='o',
                                           facecolors='none',
                                           s=50,
                                           color='black',
                                           lw=2,
                                           zorder=50)

        # Standard Deviation
        std = int(np.around(np.std([event[1] for event in self.events_glucose])))
        self.stdv.setText(str(std) + ' mg/dL')
        # color bar plot
        self.setup_slider_graph(self.stdv_bargraph)
        self.stdv_bargraph.axes.axvline(average_glucose - std,
                                        lw=3,
                                        color='black',
                                        zorder=50)
        self.stdv_bargraph.axes.axvline(average_glucose + std,
                                        lw=3,
                                        color='black',
                                        zorder=51)

        # Min/Max Glucose
        min_glucose = min([event[1] for event in self.events_glucose])
        max_glucose = max([event[1] for event in self.events_glucose])
        self.mingluc.setText(str(min_glucose) + ' mg/dL')
        self.maxgluc.setText(str(max_glucose) + ' mg/dL')

        # Average Daily Carbs
        total_on_carb_days = []
        already_seen = []
        for carb in self.events_carb:
            if not carb[0].date() in already_seen:
                already_seen.append(carb[0].date())
                carbs_on_day = carb[1]
                for other_carb in self.events_carb:
                    if other_carb[0].date() == carb[0].date():
                        carbs_on_day += other_carb[1]
                total_on_carb_days.append(carbs_on_day)
        if total_on_carb_days:
            average_on_carb_days = round(np.average(total_on_carb_days))
        else:
            average_on_carb_days = 0
        self.avgcarb.setText(str(average_on_carb_days) + ' carbs')

        ###################
        # TODO: NAME THIS
        ###################

        # refresh widgets
        self.mainplot.draw()
        self.mainplot.draw()
        self.tir_bargraph.draw()
        self.tir_piegraph.draw()
        self.avggluc_bargraph.draw()
        self.stdv_bargraph.draw()
        # FIXME: self.update()

        ###########################################################################################
        #                                   END OF PLOTTING
        ###########################################################################################

    def back_to_menu(self):
        self.start_window = StartWindow(self.ctx)
        self.start_window.show()
        self.close()

    def update_duration_label(self):
        time_a = self.time_a.dateTime().toPyDateTime()
        time_b = self.time_b.dateTime().toPyDateTime()
        delta = time_b - time_a
        days, hours = timedelta_to_string(delta.total_seconds())
        self.duration_display.setText(
            'Current Time Range:  ' + str(days) + ' days,  ' + str(hours) + ' hours')

    def on_iqrall(self):
        # self.toggle_iqr_all.setChecked(False)
        # self.toggle_iqr_eighty.setChecked(False)
        # self.toggle_iqr_fifty.setChecked(False)
        # self.event_bg.setChecked(False)
        # self.event_carb.setChecked(False)
        # self.event_exercise.setChecked(False)
        # self.event_insfast.setChecked(False)
        # self.event_inslong.setChecked(False)
        pass

    def on_iqr50(self):
        # self.toggle_iqr_all.setChecked(False)
        # self.toggle_iqr_eighty.setChecked(False)
        # self.toggle_iqr_fifty.setChecked(False)
        # self.event_bg.setChecked(False)
        # self.event_carb.setChecked(False)
        # self.event_exercise.setChecked(False)
        # self.event_insfast.setChecked(False)
        # self.event_inslong.setChecked(False)
        pass

    def on_iqr80(self):
        # self.toggle_iqr_all.setChecked(False)
        # self.toggle_iqr_eighty.setChecked(False)
        # self.toggle_iqr_fifty.setChecked(False)
        # self.event_bg.setChecked(False)
        # self.event_carb.setChecked(False)
        # self.event_exercise.setChecked(False)
        # self.event_insfast.setChecked(False)
        # self.event_inslong.setChecked(False)
        pass

    def on_bg(self):
        # self.toggle_iqr_all.setChecked(False)
        # self.toggle_iqr_eighty.setChecked(False)
        # self.toggle_iqr_fifty.setChecked(False)
        # self.event_bg.setChecked(False)
        # self.event_carb.setChecked(False)
        # self.event_exercise.setChecked(False)
        # self.event_insfast.setChecked(False)
        # self.event_inslong.setChecked(False)
        pass

    def on_carb(self):
        # self.toggle_iqr_all.setChecked(False)
        # self.toggle_iqr_eighty.setChecked(False)
        # self.toggle_iqr_fifty.setChecked(False)
        # self.event_bg.setChecked(False)
        # self.event_carb.setChecked(False)
        # self.event_exercise.setChecked(False)
        # self.event_insfast.setChecked(False)
        # self.event_inslong.setChecked(False)
        pass

    def on_exercise(self):
        # self.toggle_iqr_all.setChecked(False)
        # self.toggle_iqr_eighty.setChecked(False)
        # self.toggle_iqr_fifty.setChecked(False)
        # self.event_bg.setChecked(False)
        # self.event_carb.setChecked(False)
        # self.event_exercise.setChecked(False)
        # self.event_insfast.setChecked(False)
        # self.event_inslong.setChecked(False)
        pass

    def on_fastins(self):
        # self.toggle_iqr_all.setChecked(False)
        # self.toggle_iqr_eighty.setChecked(False)
        # self.toggle_iqr_fifty.setChecked(False)
        # self.event_bg.setChecked(False)
        # self.event_carb.setChecked(False)
        # self.event_exercise.setChecked(False)
        # self.event_insfast.setChecked(False)
        # self.event_inslong.setChecked(False)
        pass

    def on_longins(self):
        # self.toggle_iqr_all.setChecked(False)
        # self.toggle_iqr_eighty.setChecked(False)
        # self.toggle_iqr_fifty.setChecked(False)
        # self.event_bg.setChecked(False)
        # self.event_carb.setChecked(False)
        # self.event_exercise.setChecked(False)
        # self.event_insfast.setChecked(False)
        # self.event_inslong.setChecked(False)
        pass

    ########################
    # PLOTTING ADJUSTMENTS
    ########################

    #################################
    # METHODS TO READ/WRITE TO DISK
    #################################

    def read_csv(self, path=None):
        if 'glucokeep_demonstration_data' in path[0]:
            "READS DATA THAT HAS BEEN PROVIDED FOR DEMONSTRATION AND EVALUATION PURPOSES"
            print('\nDEMO FILE\n')
            return self.read_csv_demodata(path=path)
        else:
            "READS DATA THAT BELONGS TO THE PERSONAL USER"
            return self.read_csv_userdata(path=path)

    def read_csv_userdata(self, path=None):
        if not path:
            path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            # open file for reading
            with open(path[0], encoding='utf-8-sig') as csv_file:
                events = []
                my_file = csv.reader(csv_file, dialect='excel')
                for row_data in my_file:
                    date = datetime.strptime(row_data[0], '%m/%d/%Y %I:%M %p')
                    category = int(row_data[1])
                    value_one = float(row_data[2])
                    value_two = row_data[3]
                    if value_two:
                        value_two = int(value_two)
                    events.append([date, category, value_one, value_two])

        # sort events by datetime
        def time_order(event):
            return event[0]

        return sorted(events, key=time_order)

    def read_csv_demodata(self, path=None):
        """
        THIS IS A SCRIPT FOR LOADING EXAMPLE DATA TO BE USED FOR DEMONSTRATION PURPOSES ONLY.
        THIS DATA WAS DOWNLOADED FROM A REPOSITORY OF ANONYMOUS HEALTHCARE RECORDS HOSTED BY
        UC IRVINE: https://archive.ics.uci.edu/ml/datasets/diabetes

        DOCUMENTATION FOR DATASET PROVIDED UC IRVINE IS QUOTED BELOW:

        Diabetes patient records were obtained from two sources:  an automatic
        electronic recording device and paper records.  The automatic device
        had an internal clock to timestamp events, whereas the paper records
        only provided "logical time" slots (breakfast, lunch, dinner,
        bedtime).  For paper records, fixed times were assigned to breakfast
        (08:00), lunch (12:00), dinner (18:00), and bedtime (22:00).  Thus
        paper records have fictitious uniform recording times whereas
        electronic records have more realistic time stamps.

        Diabetes files consist of four fields per record.  Each field is
        separated by a tab and each record is separated by a newline.

        File Names and format:
        (1) Date in MM-DD-YYYY format
        (2) Time in XX:YY format
        (3) Code
        (4) Value

        The Code field is deciphered as follows:

        33 = Regular insulin dose
        34 = NPH insulin dose
        35 = UltraLente insulin dose
        48 = Unspecified blood glucose measurement
        57 = Unspecified blood glucose measurement
        58 = Pre-breakfast blood glucose measurement
        59 = Post-breakfast blood glucose measurement
        60 = Pre-lunch blood glucose measurement
        61 = Post-lunch blood glucose measurement
        62 = Pre-supper blood glucose measurement
        63 = Post-supper blood glucose measurement
        64 = Pre-snack blood glucose measurement
        65 = Hypoglycemic symptoms
        66 = Typical meal ingestion
        67 = More-than-usual meal ingestion
        68 = Less-than-usual meal ingestion
        69 = Typical exercise activity
        70 = More-than-usual exercise activity
        71 = Less-than-usual exercise activity
        72 = Unspecified special event


        Questions regarding the format of the diabetes data files can be sent
        to kahn@informatics.WUSTL.EDU (Internet) or 70333,34 (CompuServe).  Be
        forwarned, I'm not very good at remembering to check Compuserve.
        """

        event_types = {
            # events pertaining to glucose measurements
            'glucose measurement': [48, 57, 58, 59, 60, 61, 62, 63, 64],
            # events pertaining to the exercise intensity
            'exercise light': [71],
            'exercise moderate': [69],
            'exercise heavy': [70],
            # events pertaining to doses of fast-acting insulin
            'insulin fast-acting': [33],
            # events pertaining to doses of long-acting insulin
            'insulin long-acting': [34, 35]
        }

        if not path:
            path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            # open file for reading
            with open(path[0]) as csv_file:
                events = []
                my_file = csv.reader(csv_file, delimiter='\t')
                for row_data in my_file:
                    dt = datetime.strptime(row_data[0] + row_data[1], '%m-%d-%Y%H:%M')
                    # format according to the type of event
                    event_code = int(row_data[2])
                    if event_code in event_types['glucose measurement']:
                        events.append([dt, 0, int(row_data[3]), ''])
                    elif event_code in event_types['exercise light']:
                        events.append([dt, 2, 30, 0])
                    elif event_code in event_types['exercise moderate']:
                        events.append([dt, 2, 60, 1])
                    elif event_code in event_types['exercise heavy']:
                        events.append([dt, 2, 90, 2])
                    elif event_code in event_types['insulin fast-acting']:
                        events.append([dt, 3, float(row_data[3]), ''])
                    elif event_code in event_types['insulin long-acting']:
                        events.append([dt, 4, float(row_data[3]), ''])

        # sort events by datetime
        def time_order(event):
            return event[0]

        return sorted(events, key=time_order)

    def save_csv(self, events):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            # open for writing, truncating the file first
            with open(path[0], 'w') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in events:
                    writer.writerow(row)

    def append_to_csv(self, new_event):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            # open for writing, appending to the end of the file if it exists
            with open(path[0], 'a+') as csv_file:
                writer = csv.writer(csv_file)
                # add event as last row in the csv file
                writer.writerow(new_event)

    ###########################
    # METHODS TO SETUP WINDOW
    ###########################

    def setup_signals_and_slots(self):
        """ A method that connects PyQt5 signals and slots for this window. """

        # connect UI elements using slots and signals
        self.back_button.clicked.connect(self.back_to_menu)
        self.refresh_button.clicked.connect(self.refresh_all)
        self.toggle_iqr_all.stateChanged.connect(self.on_iqrall)
        self.toggle_iqr_eighty.stateChanged.connect(self.on_iqr80)
        self.toggle_iqr_fifty.stateChanged.connect(self.on_iqr50)
        self.event_bg.stateChanged.connect(self.on_bg)
        self.event_carb.stateChanged.connect(self.on_carb)
        self.event_exercise.stateChanged.connect(self.on_exercise)
        self.event_insfast.stateChanged.connect(self.on_fastins)
        self.event_inslong.stateChanged.connect(self.on_longins)

    def setup_time_range(self):
        """ A method that finds the time range of the entire dataset,
        then chooses a subset to work with initially. """

        # FIXME: not user-defined yet...

        # TODO: set min/max datetimes

        # only use data between the start/end dateTimes
        time_a = None
        time_b = None

        # find the newest event in the dataset
        for event in self.all_events:
            if not time_b:
                time_b = event[0]
            elif event[0] > time_b:
                time_b = event[0]

        # find the oldest event in the dataset
        for event in self.all_events:
            if not time_a:
                time_a = event[0]
            elif event[0] < time_a:
                time_a = event[0]

        # TODO: by default, initially display the most recent 30 days of data
        # time_a = time_b - timedelta(days=30)

        # convert Python's native datetime objects into PyQt5's QDateTime objects
        year_a = time_a.year
        month_a = time_a.month
        day_a = time_a.day
        hour_a = time_a.hour
        min_a = time_a.minute
        sec_a = time_a.second

        year_b = time_b.year
        month_b = time_b.month
        day_b = time_b.day
        hour_b = time_b.hour
        min_b = time_b.minute
        sec_b = time_b.second

        a = QDateTime(year_a, month_a, day_a, hour_a, min_a, sec_a, 0, 0)
        b = QDateTime(year_b, month_b, day_b, hour_b, min_b, sec_b, 0, 0)

        # visually update QDateTimeEdit widgets in the interface
        self.time_a.setDateTime(a)
        self.time_b.setDateTime(b)
        self.update_duration_label()

    def setup_initial_parameters(self):
        """ A method that sets initial values for basic interface parameters. """
        # find time range of dataset, setup QDateTimeEdit widgets
        self.setup_time_range()

        # by default, initially display only blood sugars events
        self.event_bg.setChecked(True)

    def setup_slider_graph(self, widget):
        # max_value = max([event[1] for event in self.events_glucose])
        max_value = 400
        bar_height = 1

        widget.axes.barh([1], max_value, height=bar_height, align='center',
                         color=self.color_stack[4], alpha=0.7, lw=4)
        widget.axes.barh([1], 250, height=bar_height, align='center',
                         color=self.color_stack[3], alpha=0.7)
        widget.axes.barh([1], 180, height=bar_height, align='center',
                         color=self.color_stack[2], alpha=0.7)
        widget.axes.barh([1], 70, height=bar_height, align='center',
                         color=self.color_stack[1], alpha=0.7)
        widget.axes.barh([1], 54, height=bar_height, align='center',
                         color=self.color_stack[0], alpha=0.7)
        # self.stdv_bargraph.axes.axis('off')
        widget.axes.set_xlim(0, max_value)
        widget.axes.set_ylim(0.5, 1.5)
        widget.axes.tick_params(axis='x',
                                which='both',
                                bottom=False,
                                top=False,
                                labelbottom=False)
        widget.axes.tick_params(axis='y',
                                which='both',
                                left=False,
                                right=False,
                                labelleft=False)
        """widget.axes_data.tick_params(axis='x',
                                     which='both',
                                     bottom=False,
                                     top=False,
                                     labelbottom=False)
        widget.axes_data.tick_params(axis='y',
                                     which='both',
                                     left=False,
                                     right=False,
                                     labelbottom=False)"""

        # widget.axes_data.get_xaxis().set_visible(False)
        # widget.axes_data.get_yaxis().set_visible(False)
        widget.axes.get_xaxis().set_visible(False)
        widget.axes.get_yaxis().set_visible(False)

        # widget.axes_data.xaxis.set_ticks([])
        # widget.axes_data.yaxis.set_ticks([])
        widget.axes.xaxis.set_ticks([])
        widget.axes.yaxis.set_ticks([])

        widget.setMinimumSize(1, 17)
        widget.setMaximumSize(1000, 18)
