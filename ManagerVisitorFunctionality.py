# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManagerVisitorFunctionality.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 80, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 160, 151, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 120, 151, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 240, 151, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 30, 201, 31))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 120, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 160, 111, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 80, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 200, 111, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(220, 200, 151, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(40, 240, 151, 31))
        self.pushButton_10.setObjectName("pushButton_10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Manage Profile"))
        self.pushButton_4.setText(_translate("Form", "Explore Event"))
        self.pushButton_7.setText(_translate("Form", "View Site Report"))
        self.pushButton_6.setText(_translate("Form", "Back"))
        self.label.setText(_translate("Form", "Manager Functionality"))
        self.pushButton_2.setText(_translate("Form", "View Staff"))
        self.pushButton_5.setText(_translate("Form", "Explore Site"))
        self.pushButton_3.setText(_translate("Form", "Manage Event"))
        self.pushButton_8.setText(_translate("Form", "Take Transit"))
        self.pushButton_9.setText(_translate("Form", "View Transit Hisory"))
        self.pushButton_10.setText(_translate("Form", "View Visit History"))


