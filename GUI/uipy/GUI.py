# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eee\PycharmProjects\cwodmr\GUI\ui_files\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 532)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 781, 231))
        self.widget.setObjectName("widget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(QtCore.QRect(0, 0, 70, 70)))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("C:\\Users\\eee\\Downloads\\Qlogo-White.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 260, 271, 211))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 251, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.startFreqGHzLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.startFreqGHzLabel.setObjectName("startFreqGHzLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.startFreqGHzLabel)
        self.startFreqLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.startFreqLineEdit.setObjectName("startFreqLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.startFreqLineEdit)
        self.stopFreqGHzLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.stopFreqGHzLabel.setObjectName("stopFreqGHzLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.stopFreqGHzLabel)
        self.stopFreqLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.stopFreqLineEdit.setObjectName("stopFreqLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.stopFreqLineEdit)
        self.stepFreqGHzLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.stepFreqGHzLabel.setObjectName("stepFreqGHzLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.stepFreqGHzLabel)
        self.stepsLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.stepsLineEdit.setObjectName("stepsLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.stepsLineEdit)

        self.dwellTimeMsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.dwellTimeMsLabel.setObjectName("dwellTimeMsLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.dwellTimeMsLabel)
        self.dwellTimeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.dwellTimeLineEdit.setObjectName("dwellTimeLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dwellTimeLineEdit)

        self.x_roiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.x_roiLabel.setObjectName("x_roilLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.x_roiLabel)
        self.x_roiLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.x_roiLineEdit.setObjectName("x_roilLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.x_roiLineEdit)

        self.y_roiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.y_roiLabel.setObjectName("y_roilLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.y_roiLabel)
        self.y_roiLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.y_roiLineEdit.setObjectName("y_roilLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.y_roiLineEdit)

        self.numOfAvgsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.numOfAvgsLabel.setObjectName("numOfAvgsLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.numOfAvgsLabel)
        self.numOfAvgsLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.numOfAvgsLineEdit.setObjectName("numOfAvgsLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.numOfAvgsLineEdit)
        self.powerDBLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.powerDBLabel.setObjectName("powerDBLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.powerDBLabel)
        self.powerLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.powerLineEdit.setEnabled(True)
        self.powerLineEdit.setObjectName("powerLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.powerLineEdit)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 260, 221, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButtonStart = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonStart.setGeometry(QtCore.QRect(20, 20, 93, 28))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.pushButtonStop = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonStop.setEnabled(False)
        self.pushButtonStop.setGeometry(QtCore.QRect(120, 20, 93, 28))
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 80, 201, 111))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 60, 53, 16))
        self.label.setObjectName("label")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(520, 260, 271, 211))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButtonSave = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonSave.setEnabled(False)
        self.pushButtonSave.setGeometry(QtCore.QRect(20, 20, 93, 28))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonDiscard = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonDiscard.setEnabled(False)
        self.pushButtonDiscard.setGeometry(QtCore.QRect(160, 20, 93, 28))
        self.pushButtonDiscard.setObjectName("pushButtonDiscard")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(20, 70, 231, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButtonPrev = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonPrev.setEnabled(False)
        self.pushButtonPrev.setGeometry(QtCore.QRect(20, 120, 93, 28))
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.pushButtonNext = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonNext.setGeometry(QtCore.QRect(160, 120, 93, 28))
        self.pushButtonNext.setObjectName("pushButtonNext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CW ESR"))
        self.groupBox.setTitle(_translate("MainWindow", "Parameters"))
        self.startFreqGHzLabel.setText(_translate("MainWindow", "Start Freq (GHz)"))
        self.stopFreqGHzLabel.setText(_translate("MainWindow", "Stop Freq (GHz)"))
        self.stepFreqGHzLabel.setText(_translate("MainWindow", "Num of Steps"))
        # self.dwellTimeMsLabel.setText(_translate("MainWindow", "Dwell Time (ms)"))
        self.dwellTimeMsLabel.setText(_translate("MainWindow", "Exposure Time (ms)"))
        self.x_roiLabel.setText(_translate("MainWindow", "x_roi"))
        self.y_roiLabel.setText(_translate("MainWindow", "y_roi"))
        # self.numOfAvgsLabel.setText(_translate("MainWindow", "Num of Avgs"))
        self.numOfAvgsLabel.setText(_translate("MainWindow", "Gain"))
        self.powerDBLabel.setText(_translate("MainWindow", "Power (dBm)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Control"))
        self.pushButtonStart.setText(_translate("MainWindow", "Start"))
        self.pushButtonStop.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "Log"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Data"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonDiscard.setText(_translate("MainWindow", "Discard"))
        self.pushButtonPrev.setText(_translate("MainWindow", "Previous"))
        self.pushButtonNext.setText(_translate("MainWindow", "Next"))

