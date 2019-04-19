# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisitorEventDetail.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(683, 580)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 30, 181, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 67, 17))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(120, 60, 256, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(410, 60, 67, 17))
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(460, 60, 191, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(46, 120, 81, 20))
        self.label_4.setObjectName("label_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(140, 120, 191, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(370, 130, 67, 17))
        self.label_5.setObjectName("label_5")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(450, 120, 201, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_5.setGeometry(QtCore.QRect(134, 170, 191, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(364, 180, 131, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 170, 81, 20))
        self.label_7.setObjectName("label_7")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_6.setGeometry(QtCore.QRect(500, 170, 151, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 220, 81, 20))
        self.label_8.setObjectName("label_8")
        self.textBrowser_7 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_7.setGeometry(QtCore.QRect(140, 220, 521, 241))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(50, 480, 91, 17))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 530, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 480, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(140, 480, 110, 26))
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " Event Detail"))
        self.label_2.setText(_translate("Form", "Event"))
        self.label_3.setText(_translate("Form", "Site"))
        self.label_4.setText(_translate("Form", "Start Date"))
        self.label_5.setText(_translate("Form", "End Date"))
        self.label_6.setText(_translate("Form", "Ticket Remaining"))
        self.label_7.setText(_translate("Form", "Ticket Price"))
        self.label_8.setText(_translate("Form", "Description"))
        self.label_9.setText(_translate("Form", "Visit Date"))
        self.pushButton.setText(_translate("Form", "Back"))
        self.pushButton_2.setText(_translate("Form", "Log Visit"))


