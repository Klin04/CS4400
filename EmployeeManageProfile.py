# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmployeeManageProfile.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 524)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(380, 10, 231, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 91, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 90, 141, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(540, 90, 91, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(630, 90, 141, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 130, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(160, 130, 67, 17))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(160, 130, 91, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(630, 130, 101, 21))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(540, 130, 111, 21))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(160, 160, 67, 17))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(180, 160, 91, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(70, 160, 91, 21))
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(540, 160, 81, 21))
        self.label_14.setObjectName("label_14")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(630, 160, 171, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(70, 190, 67, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(160, 190, 231, 21))
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(70, 220, 67, 17))
        self.label_15.setObjectName("label_15")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(400, 430, 141, 23))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 460, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 460, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(140, 220, 591, 151))
        self.widget.setObjectName("widget")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 10, 321, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(380, 10, 89, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Manage Profile"))
        self.label_2.setText(_translate("Form", "First Name"))
        self.label_3.setText(_translate("Form", "Last Name"))
        self.label_4.setText(_translate("Form", "Username"))
        self.label_6.setText(_translate("Form", "Fetching..."))
        self.label_7.setText(_translate("Form", "Fetching..."))
        self.label_9.setText(_translate("Form", "Site Name"))
        self.label_10.setText(_translate("Form", "Fetching..."))
        self.label_11.setText(_translate("Form", "Employee ID"))
        self.label_14.setText(_translate("Form", "Phone"))
        self.label_12.setText(_translate("Form", "Address"))
        self.label_13.setText(_translate("Form", "Fetching..."))
        self.label_15.setText(_translate("Form", "Email"))
        self.checkBox.setText(_translate("Form", "Visitor Account"))
        self.pushButton_2.setText(_translate("Form", "Update"))
        self.pushButton_3.setText(_translate("Form", "Back"))
        self.pushButton.setText(_translate("Form", "Add"))

