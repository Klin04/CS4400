# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdministratorCreateSite.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(628, 320)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 40, 91, 17))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 80, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 80, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(360, 80, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 180, 67, 17))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(170, 180, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 130, 321, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(370, 180, 131, 23))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 220, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 220, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 130, 67, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Name"))
        self.label.setText(_translate("Form", "Create Site"))
        self.label_3.setText(_translate("Form", "Zipcode"))
        self.label_5.setText(_translate("Form", "Manager"))
        self.checkBox.setText(_translate("Form", "Open Everyday"))
        self.pushButton.setText(_translate("Form", "Back"))
        self.pushButton_2.setText(_translate("Form", "Create"))
        self.label_4.setText(_translate("Form", "Address"))


