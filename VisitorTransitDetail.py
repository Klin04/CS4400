# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisitorTransitDetail.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(875, 647)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(400, 20, 111, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 67, 17))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(170, 60, 256, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(470, 70, 121, 17))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(630, 70, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(90, 140, 711, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 490, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(370, 490, 91, 17))
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(480, 490, 110, 26))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 490, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Transit Detail"))
        self.label_2.setText(_translate("Form", "Site"))
        self.label_3.setText(_translate("Form", "Transport Type"))
        self.pushButton.setText(_translate("Form", "Back"))
        self.label_4.setText(_translate("Form", "Transit Date"))
        self.pushButton_2.setText(_translate("Form", "Log Transit"))


