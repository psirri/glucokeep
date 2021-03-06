# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glucokeep_eventexercise_v5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(364, 382)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setSpacing(5)
        self.vertical_layout.setObjectName("vertical_layout")
        self.event_title = QtWidgets.QLabel(self.centralwidget)
        self.event_title.setAlignment(QtCore.Qt.AlignCenter)
        self.event_title.setObjectName("event_title")
        self.vertical_layout.addWidget(self.event_title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, -1, 11, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spin_label = QtWidgets.QLabel(self.centralwidget)
        self.spin_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.spin_label.setObjectName("spin_label")
        self.horizontalLayout.addWidget(self.spin_label)
        self.vertical_layout.addLayout(self.horizontalLayout)
        self.listwidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listwidget.sizePolicy().hasHeightForWidth())
        self.listwidget.setSizePolicy(sizePolicy)
        self.listwidget.setMaximumSize(QtCore.QSize(16777215, 79))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listwidget.setFont(font)
        self.listwidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listwidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listwidget.setObjectName("listwidget")
        item = QtWidgets.QListWidgetItem()
        self.listwidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listwidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listwidget.addItem(item)
        self.vertical_layout.addWidget(self.listwidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, -1, 11, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.desc_one = QtWidgets.QLabel(self.centralwidget)
        self.desc_one.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.desc_one.setWordWrap(True)
        self.desc_one.setObjectName("desc_one")
        self.horizontalLayout_3.addWidget(self.desc_one)
        self.vertical_layout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.vertical_layout.addWidget(self.line_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, -1, 11, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_2.addWidget(self.time_label)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setDate(QtCore.QDate(2020, 12, 8))
        self.dateTimeEdit.setTime(QtCore.QTime(8, 0, 0))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit)
        self.vertical_layout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, -1, 11, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.duration_label = QtWidgets.QLabel(self.centralwidget)
        self.duration_label.setObjectName("duration_label")
        self.horizontalLayout_5.addWidget(self.duration_label)
        self.spinbox_duration = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox_duration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinbox_duration.setMaximum(720)
        self.spinbox_duration.setSingleStep(5)
        self.spinbox_duration.setProperty("value", 30)
        self.spinbox_duration.setObjectName("spinbox_duration")
        self.horizontalLayout_5.addWidget(self.spinbox_duration)
        self.vertical_layout.addLayout(self.horizontalLayout_5)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.vertical_layout.addWidget(self.line_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, -1, 11, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.desc_two = QtWidgets.QLabel(self.centralwidget)
        self.desc_two.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.desc_two.setWordWrap(True)
        self.desc_two.setObjectName("desc_two")
        self.horizontalLayout_4.addWidget(self.desc_two)
        self.vertical_layout.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout.addItem(spacerItem1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_7.addWidget(self.save_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_7.addWidget(self.cancel_btn)
        self.vertical_layout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6.addLayout(self.vertical_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.event_title.setText(_translate("MainWindow", "Exercise"))
        self.spin_label.setText(_translate("MainWindow", "Intensity"))
        __sortingEnabled = self.listwidget.isSortingEnabled()
        self.listwidget.setSortingEnabled(False)
        item = self.listwidget.item(0)
        item.setText(_translate("MainWindow", "Light"))
        item = self.listwidget.item(1)
        item.setText(_translate("MainWindow", "Medium"))
        item = self.listwidget.item(2)
        item.setText(_translate("MainWindow", "Heavy"))
        self.listwidget.setSortingEnabled(__sortingEnabled)
        self.desc_one.setText(_translate("MainWindow", "Select the intensity of your exercise event."))
        self.time_label.setText(_translate("MainWindow", "Start"))
        self.duration_label.setText(_translate("MainWindow", "Duration"))
        self.spinbox_duration.setSuffix(_translate("MainWindow", " min"))
        self.desc_two.setText(_translate("MainWindow", "Select the start time and duration of your exercise event."))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

