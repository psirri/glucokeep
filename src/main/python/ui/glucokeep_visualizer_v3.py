# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glucokeep_visualizer_v3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1463, 870)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.vlayout_centralwidget = QtWidgets.QVBoxLayout()
        self.vlayout_centralwidget.setContentsMargins(7, 7, 7, 15)
        self.vlayout_centralwidget.setSpacing(17)
        self.vlayout_centralwidget.setObjectName("vlayout_centralwidget")
        self.hlayout_backbtn = QtWidgets.QHBoxLayout()
        self.hlayout_backbtn.setObjectName("hlayout_backbtn")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setObjectName("back_button")
        self.hlayout_backbtn.addWidget(self.back_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlayout_backbtn.addItem(spacerItem)
        self.vlayout_centralwidget.addLayout(self.hlayout_backbtn)
        self.hlayout_data = QtWidgets.QHBoxLayout()
        self.hlayout_data.setObjectName("hlayout_data")
        self.vlayout_left = QtWidgets.QVBoxLayout()
        self.vlayout_left.setObjectName("vlayout_left")
        self.frame_dates = QtWidgets.QFrame(self.centralwidget)
        self.frame_dates.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dates.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_dates.setObjectName("frame_dates")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_dates)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vlayout_dates = QtWidgets.QVBoxLayout()
        self.vlayout_dates.setObjectName("vlayout_dates")
        self.label = QtWidgets.QLabel(self.frame_dates)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.vlayout_dates.addWidget(self.label)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.time_a = QtWidgets.QDateTimeEdit(self.frame_dates)
        self.time_a.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 11, 9), QtCore.QTime(6, 0, 0)))
        self.time_a.setCalendarPopup(True)
        self.time_a.setObjectName("time_a")
        self.horizontalLayout_7.addWidget(self.time_a)
        self.label_3 = QtWidgets.QLabel(self.frame_dates)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(40, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.time_b = QtWidgets.QDateTimeEdit(self.frame_dates)
        self.time_b.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 12, 7), QtCore.QTime(22, 0, 0)))
        self.time_b.setCalendarPopup(True)
        self.time_b.setObjectName("time_b")
        self.horizontalLayout_7.addWidget(self.time_b)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.vlayout_dates.addLayout(self.horizontalLayout_7)
        self.duration_display = QtWidgets.QLabel(self.frame_dates)
        self.duration_display.setAlignment(QtCore.Qt.AlignCenter)
        self.duration_display.setObjectName("duration_display")
        self.vlayout_dates.addWidget(self.duration_display)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vlayout_dates.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.refresh_button = QtWidgets.QPushButton(self.frame_dates)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_button.sizePolicy().hasHeightForWidth())
        self.refresh_button.setSizePolicy(sizePolicy)
        self.refresh_button.setMinimumSize(QtCore.QSize(150, 0))
        self.refresh_button.setObjectName("refresh_button")
        self.horizontalLayout.addWidget(self.refresh_button)
        spacerItem5 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.vlayout_dates.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.vlayout_dates)
        self.vlayout_left.addWidget(self.frame_dates)
        self.frame_plot = QtWidgets.QFrame(self.centralwidget)
        self.frame_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plot.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_plot.setObjectName("frame_plot")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_plot)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.vlayout_plot_2 = QtWidgets.QVBoxLayout()
        self.vlayout_plot_2.setObjectName("vlayout_plot_2")
        self.mainplot = InteractivePlot(self.frame_plot)
        self.mainplot.setObjectName("mainplot")
        self.vlayout_plot_2.addWidget(self.mainplot)
        self.verticalLayout_7.addLayout(self.vlayout_plot_2)
        self.vlayout_left.addWidget(self.frame_plot)
        self.frame_iqr = QtWidgets.QFrame(self.centralwidget)
        self.frame_iqr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_iqr.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_iqr.setObjectName("frame_iqr")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_iqr)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.toggle_iqr_all = QtWidgets.QCheckBox(self.frame_iqr)
        self.toggle_iqr_all.setObjectName("toggle_iqr_all")
        self.horizontalLayout_5.addWidget(self.toggle_iqr_all)
        self.toggle_iqr_eighty = QtWidgets.QCheckBox(self.frame_iqr)
        self.toggle_iqr_eighty.setObjectName("toggle_iqr_eighty")
        self.horizontalLayout_5.addWidget(self.toggle_iqr_eighty)
        self.toggle_iqr_fifty = QtWidgets.QCheckBox(self.frame_iqr)
        self.toggle_iqr_fifty.setObjectName("toggle_iqr_fifty")
        self.horizontalLayout_5.addWidget(self.toggle_iqr_fifty)
        self.toggle_median = QtWidgets.QCheckBox(self.frame_iqr)
        self.toggle_median.setObjectName("toggle_median")
        self.horizontalLayout_5.addWidget(self.toggle_median)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.vlayout_left.addWidget(self.frame_iqr)
        self.frame_events = QtWidgets.QFrame(self.centralwidget)
        self.frame_events.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_events.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_events.setObjectName("frame_events")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_events)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.event_bg = QtWidgets.QCheckBox(self.frame_events)
        self.event_bg.setObjectName("event_bg")
        self.horizontalLayout_8.addWidget(self.event_bg)
        self.event_insfast = QtWidgets.QCheckBox(self.frame_events)
        self.event_insfast.setObjectName("event_insfast")
        self.horizontalLayout_8.addWidget(self.event_insfast)
        self.event_inslong = QtWidgets.QCheckBox(self.frame_events)
        self.event_inslong.setObjectName("event_inslong")
        self.horizontalLayout_8.addWidget(self.event_inslong)
        self.event_carb = QtWidgets.QCheckBox(self.frame_events)
        self.event_carb.setObjectName("event_carb")
        self.horizontalLayout_8.addWidget(self.event_carb)
        self.event_exercise = QtWidgets.QCheckBox(self.frame_events)
        self.event_exercise.setObjectName("event_exercise")
        self.horizontalLayout_8.addWidget(self.event_exercise)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.vlayout_left.addWidget(self.frame_events)
        self.hlayout_data.addLayout(self.vlayout_left)
        self.vlayout_right = QtWidgets.QVBoxLayout()
        self.vlayout_right.setObjectName("vlayout_right")
        self.frame_tir = QtWidgets.QFrame(self.centralwidget)
        self.frame_tir.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tir.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_tir.setObjectName("frame_tir")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_tir)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tir_label = QtWidgets.QLabel(self.frame_tir)
        self.tir_label.setObjectName("tir_label")
        self.verticalLayout_8.addWidget(self.tir_label)
        self.tir_bargraph = BarGraph(self.frame_tir)
        self.tir_bargraph.setObjectName("tir_bargraph")
        self.verticalLayout_8.addWidget(self.tir_bargraph)
        self.tir_piegraph = PieGraph(self.frame_tir)
        self.tir_piegraph.setObjectName("tir_piegraph")
        self.verticalLayout_8.addWidget(self.tir_piegraph)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.vlayout_right.addWidget(self.frame_tir)
        self.frame_dayreadings = QtWidgets.QFrame(self.centralwidget)
        self.frame_dayreadings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dayreadings.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_dayreadings.setObjectName("frame_dayreadings")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_dayreadings)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dayreadings_label = QtWidgets.QLabel(self.frame_dayreadings)
        self.dayreadings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dayreadings_label.setObjectName("dayreadings_label")
        self.horizontalLayout_2.addWidget(self.dayreadings_label)
        self.dayreadings = QtWidgets.QLabel(self.frame_dayreadings)
        self.dayreadings.setAlignment(QtCore.Qt.AlignCenter)
        self.dayreadings.setObjectName("dayreadings")
        self.horizontalLayout_2.addWidget(self.dayreadings)
        self.verticalLayout_21.addLayout(self.horizontalLayout_2)
        self.vlayout_right.addWidget(self.frame_dayreadings)
        self.frame_averagebg = QtWidgets.QFrame(self.centralwidget)
        self.frame_averagebg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_averagebg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_averagebg.setObjectName("frame_averagebg")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_averagebg)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.avggluc_label = QtWidgets.QLabel(self.frame_averagebg)
        self.avggluc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.avggluc_label.setObjectName("avggluc_label")
        self.verticalLayout_4.addWidget(self.avggluc_label)
        self.avggluc_bargraph = BarGraph(self.frame_averagebg)
        self.avggluc_bargraph.setObjectName("avggluc_bargraph")
        self.verticalLayout_4.addWidget(self.avggluc_bargraph)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.avggluc = QtWidgets.QLabel(self.frame_averagebg)
        self.avggluc.setAlignment(QtCore.Qt.AlignCenter)
        self.avggluc.setObjectName("avggluc")
        self.horizontalLayout_3.addWidget(self.avggluc)
        self.verticalLayout_15.addLayout(self.horizontalLayout_3)
        self.vlayout_right.addWidget(self.frame_averagebg)
        self.frame_stdv = QtWidgets.QFrame(self.centralwidget)
        self.frame_stdv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_stdv.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_stdv.setObjectName("frame_stdv")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_stdv)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stdv_label = QtWidgets.QLabel(self.frame_stdv)
        self.stdv_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stdv_label.setObjectName("stdv_label")
        self.verticalLayout_6.addWidget(self.stdv_label)
        self.stdv_bargraph = BarGraph(self.frame_stdv)
        self.stdv_bargraph.setObjectName("stdv_bargraph")
        self.verticalLayout_6.addWidget(self.stdv_bargraph)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.stdv = QtWidgets.QLabel(self.frame_stdv)
        self.stdv.setAlignment(QtCore.Qt.AlignCenter)
        self.stdv.setObjectName("stdv")
        self.horizontalLayout_4.addWidget(self.stdv)
        self.verticalLayout_19.addLayout(self.horizontalLayout_4)
        self.vlayout_right.addWidget(self.frame_stdv)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.mingluc_label = QtWidgets.QLabel(self.frame)
        self.mingluc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mingluc_label.setObjectName("mingluc_label")
        self.verticalLayout_10.addWidget(self.mingluc_label)
        self.mingluc = QtWidgets.QLabel(self.frame)
        self.mingluc.setAlignment(QtCore.Qt.AlignCenter)
        self.mingluc.setObjectName("mingluc")
        self.verticalLayout_10.addWidget(self.mingluc)
        self.horizontalLayout_11.addLayout(self.verticalLayout_10)
        self.horizontalLayout_10.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.maxgluc_label = QtWidgets.QLabel(self.frame_2)
        self.maxgluc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.maxgluc_label.setObjectName("maxgluc_label")
        self.verticalLayout_12.addWidget(self.maxgluc_label)
        self.maxgluc = QtWidgets.QLabel(self.frame_2)
        self.maxgluc.setAlignment(QtCore.Qt.AlignCenter)
        self.maxgluc.setObjectName("maxgluc")
        self.verticalLayout_12.addWidget(self.maxgluc)
        self.horizontalLayout_13.addLayout(self.verticalLayout_12)
        self.horizontalLayout_10.addWidget(self.frame_2)
        self.vlayout_right.addLayout(self.horizontalLayout_10)
        self.frame_avgcarbs = QtWidgets.QFrame(self.centralwidget)
        self.frame_avgcarbs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_avgcarbs.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_avgcarbs.setObjectName("frame_avgcarbs")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_avgcarbs)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.avgcarb_label = QtWidgets.QLabel(self.frame_avgcarbs)
        self.avgcarb_label.setAlignment(QtCore.Qt.AlignCenter)
        self.avgcarb_label.setObjectName("avgcarb_label")
        self.horizontalLayout_12.addWidget(self.avgcarb_label)
        self.avgcarb = QtWidgets.QLabel(self.frame_avgcarbs)
        self.avgcarb.setAlignment(QtCore.Qt.AlignCenter)
        self.avgcarb.setObjectName("avgcarb")
        self.horizontalLayout_12.addWidget(self.avgcarb)
        self.verticalLayout_13.addLayout(self.horizontalLayout_12)
        self.vlayout_right.addWidget(self.frame_avgcarbs)
        self.vlayout_right.setStretch(0, 4)
        self.vlayout_right.setStretch(1, 1)
        self.vlayout_right.setStretch(2, 2)
        self.vlayout_right.setStretch(3, 2)
        self.vlayout_right.setStretch(4, 1)
        self.vlayout_right.setStretch(5, 1)
        self.hlayout_data.addLayout(self.vlayout_right)
        self.vlayout_centralwidget.addLayout(self.hlayout_data)
        self.gridLayout.addLayout(self.vlayout_centralwidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GlucoKeep - Data Visualizer"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Choose the range of data to visualize:"))
        self.label_3.setText(_translate("MainWindow", "to"))
        self.duration_display.setText(_translate("MainWindow", "show the duration here"))
        self.refresh_button.setText(_translate("MainWindow", "Refresh"))
        self.toggle_iqr_all.setText(_translate("MainWindow", "100% of Readings"))
        self.toggle_iqr_eighty.setText(_translate("MainWindow", "80% of Readings"))
        self.toggle_iqr_fifty.setText(_translate("MainWindow", "50% of Readings"))
        self.toggle_median.setText(_translate("MainWindow", "Median"))
        self.event_bg.setText(_translate("MainWindow", "Blood Glucose"))
        self.event_insfast.setText(_translate("MainWindow", "Fast-Acting Insulin"))
        self.event_inslong.setText(_translate("MainWindow", "Long-Acting Insulin"))
        self.event_carb.setText(_translate("MainWindow", "Carbs"))
        self.event_exercise.setText(_translate("MainWindow", "Exercise"))
        self.tir_label.setText(_translate("MainWindow", "Average Daily Time in Range"))
        self.dayreadings_label.setText(_translate("MainWindow", "Average Number of\n"
"Daily Readings"))
        self.dayreadings.setText(_translate("MainWindow", "3"))
        self.avggluc_label.setText(_translate("MainWindow", "Average Glucose"))
        self.avggluc.setText(_translate("MainWindow", "167 mg/dL"))
        self.stdv_label.setText(_translate("MainWindow", "Standard Deviation"))
        self.stdv.setText(_translate("MainWindow", "72 mg/dL"))
        self.mingluc_label.setText(_translate("MainWindow", "Minimum Glucose"))
        self.mingluc.setText(_translate("MainWindow", "43 mg/dL"))
        self.maxgluc_label.setText(_translate("MainWindow", "Maximum Glucose"))
        self.maxgluc.setText(_translate("MainWindow", "318 mg/dL"))
        self.avgcarb_label.setText(_translate("MainWindow", "Average Daily Carbs"))
        self.avgcarb.setText(_translate("MainWindow", "210 carbs"))

from canvases import BarGraph, InteractivePlot, PieGraph

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

