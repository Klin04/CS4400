# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StaffVisitorFunctionality.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 180, 111, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(146, 20, 131, 31))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 140, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 180, 161, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(40, 60, 111, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 100, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 60, 111, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(210, 100, 111, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 140, 161, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_9.setText(_translate("Form", "Back"))
        self.label.setText(_translate("Form", "Staff Functionality"))
        self.pushButton_2.setText(_translate("Form", "Take Transit"))
        self.pushButton_3.setText(_translate("Form", "View Transit History"))
        self.pushButton_8.setText(_translate("Form", "Manage Profile"))
        self.pushButton.setText(_translate("Form", "View Schedule"))
        self.pushButton_10.setText(_translate("Form", "Explore Event"))
        self.pushButton_11.setText(_translate("Form", "Explore Site"))
        self.pushButton_4.setText(_translate("Form", "View Visit History"))


