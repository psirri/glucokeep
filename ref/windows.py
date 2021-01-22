"""
windows.py -- Links components of the graphical user interface.
Copyright (C) 2020  Paul Sirri <paulsirri@gmail.com>

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

# File Description:
# This file contains the logic for linking together the components of
# the graphical user interface. In the UI directory, custom PyQt5
# QMainWindow classes are defined. Here, those custom classes are
# wrapped, given functionality, and linked together.


from PyQt5.QtGui import QImage, QPixmap, QGuiApplication
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QAbstractItemView, QTableWidget, \
    QTableWidgetItem, QDialog, QProgressBar, QPushButton, QApplication, QTabWidget, QWidget, \
    QVBoxLayout, QLabel

from ui.ui_20201106.StartScreen_v18 import Ui_MainWindow as Start_Ui
# from ui.ui_20201106.FileSelection_v18_dawn import Ui_MainWindow as File_Ui
from ui.ui_20200906.FileSelection_v13 import Ui_MainWindow as File_Ui
from ui.ui_20201106.SignalAnalysis_v18 import Ui_MainWindow as Signal_Ui

from read_data import find_polar_pair, file_to_numpy, get_iq_data, get_files, get_sample_rate
from process_signal import get_settings
from analyze_plot import analyze_plot
import numpy as np
import time

import matplotlib

matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class StartWindow(QMainWindow, Start_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super(StartWindow, self).__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)
        print("\nStartWindow.__init__()")

        """img_usc = QImage(self.ctx.img_usc())
        pixmap_usc = QPixmap(img_usc)
        pixmap_usc = pixmap_usc.scaled(400, 400, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap_usc)
        # label.setPixmap(QPixmap.fromImage(self.ctx.img_bomb))"""

        img_parse = QImage(self.ctx.img_parse())
        pixmap_parse = QPixmap(img_parse)
        pixmap_parse = pixmap_parse.scaled(400, 400, Qt.KeepAspectRatio)
        self.label_2.setPixmap(pixmap_parse)

        self.btn_open.clicked.connect(self.choose_directory)

    def choose_directory(self):
        self.directory = QFileDialog.getExistingDirectory()
        # self.directory = 'data/dawn/'
        print("chose directory: " + str(self.directory))

        if self.directory:
            self.show_file_window()
        else:
            # TODO: implement error dialog
            print("implement directory error")

    def show_file_window(self):
        # FIXME: lambda signal/slot?
        print('StartWindow.show_file_window(self)')
        self.file_window = FileWindow(self.ctx, self.directory)
        self.file_window.show()
        self.hide()


class FileWindow(QMainWindow, File_Ui):
    def __init__(self, ctx, directory, *args, **kwargs):
        super(FileWindow, self).__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)
        print("\nFileWindow.__init__()")

        # save session variables
        self.directory = directory

        # read label files in directory, add to selection table
        self.data_labels = get_files(directory)
        self.fill_table()

        # when a row is clicked, pass file info to next window
        self.table_files.itemSelectionChanged.connect(self.display_label)

        self.selected_file = None

        # connect buttons
        self.btn_back.clicked.connect(self.back_to_start)
        self.btn_process.clicked.connect(self.show_signal_window)

        # self.show()

    def fill_table(self):
        # format table
        column_names = ['File Name', 'Start Time', 'Stop Time', 'Band', 'Polarization']
        self.table_files.setColumnCount(5)
        self.table_files.setRowCount(len(self.data_labels))
        self.table_files.setHorizontalHeaderLabels(column_names)

        # fill with file metadata
        for row in range(len(self.data_labels)):
            # set values for each item in row
            self.table_files.setItem(row, 0, QTableWidgetItem(self.data_labels[row].file_name))
            self.table_files.setItem(row, 1, QTableWidgetItem(str(
                self.data_labels[row].start_time)))
            self.table_files.setItem(row, 2, QTableWidgetItem(str(
                self.data_labels[row].stop_time)))
            self.table_files.setItem(row, 3, QTableWidgetItem(
                self.data_labels[row].band_name))
            self.table_files.setItem(row, 4, QTableWidgetItem(
                self.data_labels[row].polarization))

        # set QTableWidget formatting properties
        self.table_files.resizeColumnsToContents()
        self.table_files.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_files.setEditTriggers(QTableWidget.NoEditTriggers)

        print("table filled")

    def display_label(self):
        for lbl in self.data_labels:
            if lbl.file_name == self.table_files.selectedItems()[0].text():
                # the selected row matches a data_label object
                self.selected_file = lbl
                # some missions may not use label files
                if lbl.path_to_label:
                    # read the label file, print to UI
                    f = open(lbl.path_to_label, 'r')
                    file_contents = f.read()
                    f.close()
                    self.lbl_quickview.setText(file_contents)
                print("selected label: " + str(self.selected_file.file_name))

    def back_to_start(self):
        # FIXME: lambda signal/slot?
        print('FileWindow.back_to_start(self)')
        self.start_window = StartWindow(self.ctx)
        self.start_window.show()
        self.hide()

    def show_signal_window(self):
        # FIXME: lambda signal/slot?
        self.files_tuple = find_polar_pair(self.selected_file, self.data_labels)
        print('FileWindow.show_signal_window(self)')
        self.signal_window = SignalWindow(self.ctx, self.directory, self.files_tuple)
        self.signal_window.show()
        self.hide()


class SignalWindow(QMainWindow, Signal_Ui):
    signal_to_run_worker = QtCore.pyqtSignal(object, object)
    signal_to_plot_analysis_results = QtCore.pyqtSignal(object)
    signal_to_hide_analysis_results = QtCore.pyqtSignal()

    def __init__(self, ctx, directory, files_tuple, *args, **kwargs):
        super(SignalWindow, self).__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)
        print("\nSignalWindow.__init__()")

        self.tab_widget.setTabEnabled(1, False)

        ###############################################
        # set stylesheets
        # self.group_aq_geometry.setStyleSheet()
        ###############################################

        # create toolbar, passing canvas as first parameter, then parent
        toolbar = NavigationToolbar(self.animation_widget, self)
        self.vlayout_right.insertWidget(2, toolbar)

        # TODO: thread to handle data ingestion
        # Create a WorkerDataIngestion object and a thread
        self.worker_dataingestion = WorkerDataIngestion()
        self.worker_dataingestion_thread = QtCore.QThread()

        # Assign the worker_dataingestion to the thread and start the thread
        self.worker_dataingestion.moveToThread(self.worker_dataingestion_thread)
        self.worker_dataingestion_thread.start()

        # dialog box to show worker progress
        self.progress_window = IngestionProgress(parent=self)
        # self.progress_window.setFocus(True)
        # self.progress_window.raise_()
        # self.progress_window.activateWindow()

        print('Data Ingestion: connecting signals to slots')

        # Connect signals & slots AFTER moving the object to the thread
        # connect worker_dataingestion.signal_to_return_data (signal) to self.receive_data_from_worker (slot)
        self.worker_dataingestion.signal_to_return_data.connect(self.receive_data_from_worker)
        # connect worker_dataingestion.signal_progress_changed (signal) to self.progress_window.receive_progress (slot)
        self.worker_dataingestion.signal_progress_changed.connect(self.progress_window.receive_progress)
        # connect self.signal_to_run_worker (signal) to worker_dataingestion.run (slot)
        self.signal_to_run_worker.connect(self.worker_dataingestion.run)
        # connect self.signal_to_plot_analysis_results (signal) to self.animation_widget.plot_analysis_results (slot)
        self.signal_to_plot_analysis_results.connect(self.animation_widget.plot_analysis_results)
        # connect self.signal_to_hide_analysis_results (signal) to self.animation_widget.plot_analysis_results (slot)
        self.signal_to_hide_analysis_results.connect(self.animation_widget.hide_analysis_results)

        # save current directory
        self.directory = directory

        # unpack selected files
        self.rcp_file, self.lcp_file = files_tuple

        # initialize values to be returned by worker
        self.rcp_processed = None
        self.lcp_processed = None
        self.rcp_data = None
        self.lcp_data = None
        self.sample_rate = None
        self.current_settings = None
        self.current_settings_rounded = None
        self.msmt = None

        # TODO: receive data
        self.signal_to_run_worker.emit(self.rcp_file, self.lcp_file)

        # connect buttons for general interface
        self.btn_back.clicked.connect(self.back_to_files)
        self.btn_apply_changes.clicked.connect(self.apply_changes)
        self.btn_refresh_plot.clicked.connect(self.apply_changes_plot_analysis)
        self.tab_widget.currentChanged.connect(self.toggle_results)
        # connect buttons that control animation playback
        self.btn_play.clicked.connect(self.play_animation)
        self.btn_pause.clicked.connect(self.pause_animation)
        self.btn_prev_frame.clicked.connect(self.animation_widget.show_previous_frame)
        self.btn_prev_frame.clicked.connect(self.pause_animation)
        self.btn_next_frame.clicked.connect(self.animation_widget.show_next_frame)
        self.btn_next_frame.clicked.connect(self.pause_animation)

    def show_parameters(self, s):
        """ A method to set the value of each QSpinBox widget on the Signal Processing tab. """

        print('SignalAnalysis.show_parameters()')

        # row 1 of Signal Processing tab
        self.line_edit_target.setText(s.target)
        self.line_edit_mission.setText(s.mission)

        # row 2 of Signal Processing tab
        self.spin_occ_duration.setValue(np.floor(s.dt_occ / 60))
        self.spin_eq_radius.setValue(np.floor(s.radius_target / 1000))

        # row 3 of Signal Processing tab
        self.spin_sc_velocity.setValue(s.v_sc_orbital)
        self.spin_lowest_alt.setValue(np.floor(s.altitude_sc / 1000))

        # row 4 of Signal Processing tab
        self.spin_freq_separation.setValue(s.δf_calc)
        self.spin_freq_res.setValue(s.freq_res)

        # row 5 of Signal Processing tab
        self.spin_l_win.setValue(s.samples_per_raw_fft)
        self.spin_t_int.setValue(s.seconds_per_raw_fft)

        # row 6 of Signal Processing tab
        self.spin_k_spec.setValue(s.raw_fft_per_average)
        self.spin_timespan.setValue(s.seconds_for_welch)

        # row 7 of Signal Processing tab
        self.spin_moving_overlap.setValue(s.percent_window_per_hop)
        self.spin_t_hop.setValue(s.seconds_per_hop)

        # row 8 of Signal Processing tab
        self.spin_xmin.setValue(s.xlim_min)
        self.spin_xmax.setValue(s.xlim_max)

        # row 9 of Signal Processing tab
        self.spin_ymin.setValue(s.ylim_min)
        self.spin_ymax.setValue(s.ylim_max)

        # row 10 of Signal Processing tab
        self.spin_start_sec.setMaximum(np.floor((self.rcp_file.stop_time - self.rcp_file.start_time).to_value('sec')))
        self.spin_start_sec.setValue(s.start_sec_user)
        self.spin_ani_speed.setValue(round(1000 / s.interval, 2))

        # make a copy of these rounded values, in order to keep track of changes made by user
        self.current_settings_rounded = {
            'line_edit_target': self.line_edit_target.text(),
            'line_edit_mission': self.line_edit_mission.text(),
            'spin_occ_duration': self.spin_occ_duration.value(),
            'spin_eq_radius': self.spin_eq_radius.value(),
            'spin_sc_velocity': self.spin_sc_velocity.value(),
            'spin_lowest_alt': self.spin_lowest_alt.value(),
            'spin_freq_separation': self.spin_freq_separation.value(),
            'spin_freq_res': self.spin_freq_res.value(),
            'spin_l_win': self.spin_l_win.value(),
            'spin_t_int': self.spin_t_int.value(),
            'spin_k_spec': self.spin_k_spec.value(),
            'spin_timespan': self.spin_timespan.value(),
            'spin_moving_overlap': self.spin_moving_overlap.value(),
            'spin_t_hop': self.spin_t_hop.value(),
            'spin_xmin': self.spin_xmin.value(),
            'spin_xmax': self.spin_xmax.value(),
            'spin_ymin': self.spin_ymin.value(),
            'spin_ymax': self.spin_ymax.value(),
            'spin_start_sec': self.spin_start_sec.value(),
            'spin_ani_speed': self.spin_ani_speed.value(),
        }

    def apply_changes(self):
        """ A method to read the user input parameters from QSpinBox widgets on
        the Signal Processing tab, generate a new ProgramSettings object, then pass
        these new settings into the animation widget for plotting.

        NOTE: Some of the values had to be rounded when they were initially printed
        to the Signal Processing tab. So, when reading these values back in, the
        values can't be copied exactly, as precision may have been lost to rounding.
        To address this issue, the code below measures the amount by which the user
        changed each parameter, then adds this difference to the initial value.

        Example:
        new_value_in_code = ( new_value_in_GUI - old_value_in_GUI ) + old_value_in_code

        """

        print('\n\n---------------------------------------\n\nSignalAnalysis.apply_changes()\n\n')

        # signals to stop generating old plots
        self.animation_widget.pause_worker()
        self.animation_widget.kill_worker()

        # ensure the old data has been cleared from queues
        self.animation_widget.plots = []
        self.animation_widget.frame_index = 0

        # row 1 of Signal Processing tab
        target = self.line_edit_target.text()
        mission = self.line_edit_mission.text()

        # row 2 of Signal Processing tab
        dt_occ = round(((self.spin_occ_duration.value() - self.current_settings_rounded['spin_occ_duration']) * 60) + self.current_settings.dt_occ)
        radius_target = ((self.spin_eq_radius.value() - self.current_settings_rounded['spin_eq_radius']) * 1000) + self.current_settings.radius_target

        # row 3 of Signal Processing tab
        v_sc_orbital = (self.spin_sc_velocity.value() - self.current_settings_rounded['spin_sc_velocity']) + self.current_settings.v_sc_orbital
        altitude_sc = ((self.spin_lowest_alt.value() - self.current_settings_rounded['spin_lowest_alt']) * 1000) + self.current_settings.altitude_sc

        # row 4 of Signal Processing tab
        # δf_calc = NOT ADJUSTABLE (self.spin_freq_separation.value())
        freq_res = (self.spin_freq_res.value() - self.current_settings_rounded['spin_freq_res']) + self.current_settings.freq_res

        # row 5 of Signal Processing tab
        # samples_per_raw_fft = NOT ADJUSTABLE (self.spin_l_win.value())
        # seconds_per_raw_fft = NOT ADJUSTABLE (self.spin_t_int.value())

        # row 6 of Signal Processing tab
        raw_fft_per_average = round((self.spin_k_spec.value() - self.current_settings_rounded['spin_k_spec']) + self.current_settings.raw_fft_per_average)

        # handle specially, seconds_for_welch is dependent on, and a dependent of, other parameters
        if self.spin_timespan.value() != self.current_settings_rounded['spin_timespan']:
            # user manually entered value for seconds_for_welch, use to calculate other params
            seconds_for_welch_user = (self.spin_timespan.value() - self.current_settings_rounded['spin_timespan']) + self.current_settings.seconds_for_welch
        else:
            # user did not adjust seconds_for_welch, just use defaults in calculations
            seconds_for_welch_user = None

        # row 7 of Signal Processing tab
        percent_window_per_hop = (self.spin_moving_overlap.value() - self.current_settings_rounded['spin_moving_overlap']) + self.current_settings.percent_window_per_hop
        # seconds_per_hop = NOT ADJUSTABLE (self.spin_t_hop.value())

        # row 8 of Signal Processing tab
        xlim_min = (self.spin_xmin.value() - self.current_settings_rounded['spin_xmin']) + self.current_settings.xlim_min
        xlim_max = (self.spin_xmax.value() - self.current_settings_rounded['spin_xmax']) + self.current_settings.xlim_max

        # row 9 of Signal Processing tab
        ylim_min = (self.spin_ymin.value() - self.current_settings_rounded['spin_ymin']) + self.current_settings.ylim_min
        ylim_max = (self.spin_ymax.value() - self.current_settings_rounded['spin_ymax']) + self.current_settings.ylim_max

        # row 10 of Signal Processing tab
        start_sec_user = round(self.spin_start_sec.value())
        frames_per_second = self.spin_ani_speed.value()
        # convert to milliseconds
        interval = round(1000 / frames_per_second)

        # make new version of ProgramSettings
        # get all parameters for radar analysis pipeline, using RCP file to set default values
        new_settings = get_settings(filenames=(self.rcp_file.file_name, self.lcp_file.file_name),
                                    rcp_data=self.rcp_data,
                                    lcp_data=self.lcp_data,
                                    sample_rate=self.sample_rate,
                                    band_name=self.rcp_file.band_name,
                                    global_time=self.rcp_file.start_time,
                                    target=target, mission=mission,
                                    dt_occ=dt_occ, radius_target=radius_target,
                                    v_sc_orbital=v_sc_orbital, altitude_sc=altitude_sc,
                                    δf_calc=None, freq_res=freq_res,
                                    samples_per_raw_fft=None, seconds_per_raw_fft=None,
                                    raw_fft_per_average=raw_fft_per_average,
                                    seconds_for_welch_user=seconds_for_welch_user,
                                    percent_window_per_hop=percent_window_per_hop,
                                    seconds_per_hop=None,
                                    xlim_min=xlim_min, xlim_max=xlim_max,
                                    ylim_min=ylim_min, ylim_max=ylim_max,
                                    start_sec_user=start_sec_user, interval=interval,
                                    file_start_time=self.rcp_file.start_time,
                                    file_end_time=self.rcp_file.stop_time)

        # TODO: use signal/slot

        # keep track of current settings
        self.current_settings = new_settings

        # show new parameters to user
        self.show_parameters(new_settings)

        # pass new parameters into animation widget, initialize plot
        self.setup_animation(new_settings, self.rcp_data, self.lcp_data)

    def show_parameters_plot_analysis(self, msmt):
        """ A method to set the value of each QSpinBox widget on the Spectral Analysis tab. """

        print('SignalAnalysis.show_parameters_plot_analysis()')

        self.spin_measure_bandwidth_below.setValue(msmt.NdB_below)
        self.spin_x_min.setValue(msmt.freq_local_min)
        self.spin_x_max.setValue(msmt.freq_local_max)

        self.spin_ymax_global.setValue(msmt.Pxx_max)
        self.spin_x_at_ymax_global.setValue(msmt.freq_at_max)
        self.spin_bandwidth_global.setValue(msmt.bandwidth_of_max)
        self.spin_noise_variance_global.setValue(msmt.Pxx_noise_var)
        self.spin_delta_x_predict.setValue(msmt.δf_calc)

        self.spin_ymax_local.setValue(msmt.Pxx_local_max)
        self.spin_x_at_ymax_local.setValue(msmt.freq_at_local_max)
        self.spin_bandwidth_local.setValue(msmt.bandwidth_local_peak)
        self.spin_variance_local.setValue(msmt.Pxx_local_var)
        self.spin_delta_y.setValue(msmt.dPxx_max)
        self.spin_delta_x_observed.setValue(msmt.δf_obsv)

    def apply_changes_plot_analysis(self):
        """ A method to read the user input parameters from QSpinBox widgets
        on the Signal Analysis tab, generate a new SignalAnalysis object, then
        pass these results into the animation widget. """

        NdB_below = int(round(self.spin_measure_bandwidth_below.value()))
        freq_local_min = int(round(self.spin_x_min.value()))
        freq_local_max = int(round(self.spin_x_max.value()))

        # get measurements for plot analysis, using data from RCP file
        msmt = analyze_plot(s=self.animation_widget.s,
                            freqs=self.animation_widget.plots[self.animation_widget.frame_index][0],
                            Pxx=self.animation_widget.plots[self.animation_widget.frame_index][1],
                            NdB_below=NdB_below,
                            freq_local_min=freq_local_min,
                            freq_local_max=freq_local_max)

        self.msmt = msmt

        # show new parameters to user
        self.show_parameters_plot_analysis(msmt)

        # pass new parameters into animation widget, initialize plot
        # TODO: send results to animation for plotting

        is_calculated = True
        if msmt.error_NdB_below:
            is_calculated = False
            self.show_error_message('Error: Bandwidth cannot be measured this far below peak.')
        if msmt.error_direct_signal:
            is_calculated = False
            self.show_error_message('Warning: local max may not be a signal; detectability limit is >= 3 dB above the noise.')
        if msmt.error_finding_bandwidth:
            is_calculated = False
            self.show_error_message('Error: Unable to detect the bandwidth of the specified peak.')
        if is_calculated:
            self.signal_to_plot_analysis_results.emit(msmt)

    def toggle_results(self):
        print("\nSignalWindow.toggle_results()\n")
        if self.tab_widget.currentIndex() == 1:
            # get measurements for plot analysis using data from current RCP frame, use defaults
            msmt = analyze_plot(s=self.animation_widget.s,
                                freqs=self.animation_widget.plots[self.animation_widget.frame_index][0],
                                Pxx=self.animation_widget.plots[self.animation_widget.frame_index][1])

            self.msmt = msmt

            # print values to QSpinBoxes on Signal Analysis tab
            self.show_parameters_plot_analysis(msmt)

            # provide error messages to help user diagnose issues
            is_calculated = True
            if self.msmt.error_NdB_below:
                is_calculated = False
                self.show_error_message('Error: Bandwidth cannot be measured this far below peak.')
            if self.msmt.error_direct_signal:
                is_calculated = False
                self.show_error_message('Warning: local max may not be a signal; detectability limit is >= 3 dB above the noise.')
            if self.msmt.error_finding_bandwidth:
                is_calculated = False
                self.show_error_message('Error: Unable to detect the bandwidth of the specified peak.')
            if is_calculated:
                self.signal_to_plot_analysis_results.emit(self.msmt)
        elif self.tab_widget.currentIndex() == 0:
            # hide results
            print("hide results")
            self.signal_to_hide_analysis_results.emit()

    def setup_animation(self, s, rcp_data, lcp_data):
        print("\nSignalWindow.setup_animation()")
        self.animation_widget.setup(s, rcp_data, lcp_data)
        # TODO: QDialog to ask if the user wants to reset the currently running animation

    def play_animation(self):
        print("\nSignalWindow.play_animation()")
        self.animation_widget.play()

        # only allow the user to analyze a plot if the animation is paused
        self.tab_widget.setTabEnabled(1, False)

    def pause_animation(self):
        print("\nSignalWindow.pause_animation()")
        self.animation_widget.pause()

        # only allow the user to analyze a plot if the animation is paused
        self.tab_widget.setTabEnabled(1, True)

    def export_animation(self):
        # print('export attempted')
        pass

    def back_to_files(self):
        # FIXME: lambda signal/slot?
        print('SignalWindow.back_to_files(self)')
        self.pause_animation()
        self.file_window = FileWindow(self.ctx, self.directory)
        self.file_window.show()
        self.hide()

    def show_error_message(self, message):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(message)
        error_dialog.exec_()

    @QtCore.pyqtSlot(object)
    def receive_data_from_worker(self, data_tuple):
        """ A method to queue up frames for the animation to plot. """

        self.progress_window.hide()
        self.rcp_processed = data_tuple[0]
        self.lcp_processed = data_tuple[1]
        self.rcp_data = data_tuple[2]
        self.lcp_data = data_tuple[3]
        self.sample_rate = data_tuple[4]
        self.current_settings = data_tuple[5]

        # show default parameters to user
        self.show_parameters(data_tuple[5])

        # pass default parameters into animation widget, initialize plot
        self.setup_animation(data_tuple[5], self.rcp_data, self.lcp_data)


class WorkerDataIngestion(QtCore.QObject):
    """ A class that functions as a worker, generating plots from a separate thread. """

    signal_to_return_data = QtCore.pyqtSignal(object)
    signal_progress_changed = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        # QtCore.QObject.__init__(self, parent=parent)
        super(WorkerDataIngestion, self).__init__(parent)

    @QtCore.pyqtSlot(object, object)
    def run(self, rcp_file, lcp_file):
        print('SLOT: WorkerDataIngestion.run(rcp_file, lcp_file)\n')

        # read data files into Numpy
        rcp_processed = file_to_numpy(rcp_file)
        self.signal_progress_changed.emit(10)
        lcp_processed = file_to_numpy(lcp_file)
        self.signal_progress_changed.emit(20)

        # isolate IQ data from processed file
        rcp_data = get_iq_data(rcp_processed, rcp_file.mission)
        self.signal_progress_changed.emit(40)

        lcp_data = get_iq_data(lcp_processed, lcp_file.mission)
        self.signal_progress_changed.emit(60)

        # get the sample rate of the data file
        sample_rate = get_sample_rate(rcp_processed, rcp_file.mission)
        self.signal_progress_changed.emit(70)

        print(rcp_file.mission)
        print(type(rcp_file.mission))

        # get all parameters for radar analysis pipeline, using RCP file to set default values
        s = get_settings(filenames=(rcp_file.file_name, lcp_file.file_name),
                         rcp_data=rcp_data,
                         lcp_data=lcp_data,
                         sample_rate=sample_rate,
                         band_name=rcp_file.band_name,
                         global_time=rcp_file.start_time,
                         mission=rcp_file.mission,
                         file_start_time=rcp_file.start_time,
                         file_end_time=rcp_file.stop_time)

        self.signal_progress_changed.emit(95)
        time.sleep(0.20)
        self.signal_progress_changed.emit(100)
        print('sleeping...')
        time.sleep(0.15)

        self.signal_to_return_data.emit((rcp_processed, lcp_processed, rcp_data, lcp_data,
                                         sample_rate, s))


class IngestionProgress(QDialog):
    """
    Simple dialog that consists of a Progress Bar and a Button.
    Clicking on the button results in the start of a timer and
    updates the progress bar.
    """

    def __init__(self, parent=None):
        super(IngestionProgress, self).__init__(parent)
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle('Loading Data Files')
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        self.setModal(True)

        screen_geometry = QGuiApplication.screens()[0].geometry()
        x = (screen_geometry.width() - self.width()) / 2
        y = ((screen_geometry.height() - self.height()) / 2) - (screen_geometry.height() * 0.05)
        self.move(x, y)
        print(screen_geometry.width())
        print(screen_geometry.height())

        # self.button = QPushButton('Start', self)
        # self.button.move(0, 30)

        # self.button.clicked.connect(self.onButtonClick)

    @QtCore.pyqtSlot(int)
    def receive_progress(self, count):
        print(count)
        self.progress.setValue(count)
        print('value: ', self.progress.value())