# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glucokeep_startscreen_v1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 390)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_appheader = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_appheader.sizePolicy().hasHeightForWidth())
        self.label_appheader.setSizePolicy(sizePolicy)
        self.label_appheader.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_appheader.setFont(font)
        self.label_appheader.setAlignment(QtCore.Qt.AlignCenter)
        self.label_appheader.setObjectName("label_appheader")
        self.verticalLayout.addWidget(self.label_appheader)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_addevent = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addevent.sizePolicy().hasHeightForWidth())
        self.btn_addevent.setSizePolicy(sizePolicy)
        self.btn_addevent.setMinimumSize(QtCore.QSize(180, 80))
        self.btn_addevent.setObjectName("btn_addevent")
        self.horizontalLayout.addWidget(self.btn_addevent)
        self.btn_visualize = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_visualize.sizePolicy().hasHeightForWidth())
        self.btn_visualize.setSizePolicy(sizePolicy)
        self.btn_visualize.setMinimumSize(QtCore.QSize(180, 80))
        self.btn_visualize.setObjectName("btn_visualize")
        self.horizontalLayout.addWidget(self.btn_visualize)
        self.btn_about = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_about.sizePolicy().hasHeightForWidth())
        self.btn_about.setSizePolicy(sizePolicy)
        self.btn_about.setMinimumSize(QtCore.QSize(180, 80))
        self.btn_about.setObjectName("btn_about")
        self.horizontalLayout.addWidget(self.btn_about)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_appheader.setText(_translate("MainWindow", "GlucoKeep"))
        self.btn_addevent.setText(_translate("MainWindow", "Add Event"))
        self.btn_visualize.setText(_translate("MainWindow", "Visualize"))
        self.btn_about.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

