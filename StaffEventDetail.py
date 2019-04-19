# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StaffEventDetail.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(703, 690)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 20, 181, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 67, 17))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(100, 60, 256, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(400, 60, 67, 17))
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(480, 60, 171, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 81, 17))
        self.label_4.setObjectName("label_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(130, 100, 171, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(350, 100, 81, 17))
        self.label_5.setObjectName("label_5")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(430, 100, 171, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 150, 101, 17))
        self.label_6.setObjectName("label_6")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_5.setGeometry(QtCore.QRect(150, 150, 111, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 200, 111, 17))
        self.label_7.setObjectName("label_7")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_6.setGeometry(QtCore.QRect(160, 200, 131, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_7.setGeometry(QtCore.QRect(400, 200, 131, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(320, 200, 111, 17))
        self.label_8.setObjectName("label_8")
        self.textBrowser_8 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_8.setGeometry(QtCore.QRect(130, 250, 131, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(40, 250, 111, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(40, 300, 111, 17))
        self.label_10.setObjectName("label_10")
        self.textBrowser_9 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_9.setGeometry(QtCore.QRect(130, 300, 531, 241))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 570, 89, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Event Detail"))
        self.label_2.setText(_translate("Form", "Event"))
        self.label_3.setText(_translate("Form", "Site"))
        self.label_4.setText(_translate("Form", "Start Date"))
        self.label_5.setText(_translate("Form", "End Date"))
        self.label_6.setText(_translate("Form", "Duration Days"))
        self.label_7.setText(_translate("Form", "Staffs Assigned"))
        self.label_8.setText(_translate("Form", "Capacity"))
        self.label_9.setText(_translate("Form", "Capacity"))
        self.label_10.setText(_translate("Form", "Description"))
        self.pushButton.setText(_translate("Form", "Back"))


