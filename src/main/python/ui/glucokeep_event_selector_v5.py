# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glucokeep_event_selector_v5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(364, 327)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setSpacing(0)
        self.vertical_layout.setObjectName("vertical_layout")
        self.glucose_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glucose_button.sizePolicy().hasHeightForWidth())
        self.glucose_button.setSizePolicy(sizePolicy)
        self.glucose_button.setObjectName("glucose_button")
        self.vertical_layout.addWidget(self.glucose_button)
        self.carbs_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carbs_button.sizePolicy().hasHeightForWidth())
        self.carbs_button.setSizePolicy(sizePolicy)
        self.carbs_button.setObjectName("carbs_button")
        self.vertical_layout.addWidget(self.carbs_button)
        self.exercise_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exercise_button.sizePolicy().hasHeightForWidth())
        self.exercise_button.setSizePolicy(sizePolicy)
        self.exercise_button.setObjectName("exercise_button")
        self.vertical_layout.addWidget(self.exercise_button)
        self.insfast_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.insfast_button.sizePolicy().hasHeightForWidth())
        self.insfast_button.setSizePolicy(sizePolicy)
        self.insfast_button.setObjectName("insfast_button")
        self.vertical_layout.addWidget(self.insfast_button)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.vertical_layout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout.addItem(spacerItem)
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setObjectName("cancel_btn")
        self.vertical_layout.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.vertical_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.glucose_button.setText(_translate("MainWindow", "Blood Glucose"))
        self.carbs_button.setText(_translate("MainWindow", "Carbs"))
        self.exercise_button.setText(_translate("MainWindow", "Exercise"))
        self.insfast_button.setText(_translate("MainWindow", "Fast-Acting Insulin"))
        self.pushButton_2.setText(_translate("MainWindow", "Long-Acting Insulin"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

