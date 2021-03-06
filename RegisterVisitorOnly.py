# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterVisitorOnly.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self):
        self.EditLineList = []
        self.EmailRemoveButtons = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(643, 410)
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 190, 171, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 50, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 360, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 50, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 50, 81, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 360, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 100, 113, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 71, 17))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 50, 81, 31))
        self.label.setObjectName("label")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 150, 171, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 131, 17))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(210, 0, 131, 41))
        self.label_8.setObjectName("label_8")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(30, 240, 67, 17))
        self.label_14.setObjectName("label_14")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 360, 89, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.addEmail)

        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)

        self.widget = QtWidgets.QScrollArea(Form)
        self.widget.setGeometry(QtCore.QRect(90, 230, 521, 101))
        self.widget.setObjectName("widget")
        self.widget.setWidgetResizable(True)
        self.widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # set Qframe within QScroll Area to add and remove items
        self.inner = QtWidgets.QFrame(self.widget)
        self.inner.setLayout(QtWidgets.QVBoxLayout())
        self.widget.setWidget(self.inner)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def addEmail(self):
        # add the edit line
        line_text = QtWidgets.QLineEdit(self.widget)
        self.EditLineList.append(line_text)
        line_text.setGeometry(QtCore.QRect(20, 10, 301, 25))
        self.inner.layout().addWidget(line_text)
        # now add the remove button and set listener
        new_button = QtWidgets.QPushButton(self.widget)
        self.EmailRemoveButtons.append(new_button)
        new_button.setText("Remove")
        self.inner.layout().addWidget(new_button)
        # since we can't pass arguments into .connect, we pass in the lambda as a func
        new_button.clicked.connect(lambda: self.removeEmail(new_button))

    def removeEmail(self, button):
        if len(self.EditLineList) == 0:
            return
        # find the button and editline to delete
        index = self.EmailRemoveButtons.index(button)
        # delete the button
        self.inner.layout().removeWidget(self.EditLineList[index])
        self.EditLineList[index].deleteLater()
        self.EditLineList.pop(index)
        # delete the button
        self.inner.layout().removeWidget(self.EmailRemoveButtons[index])
        self.EmailRemoveButtons[index].deleteLater()
        self.EmailRemoveButtons.pop(index)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_3.setText(_translate("Form", "Register"))
        self.label_4.setText(_translate("Form", "Password"))
        self.label_2.setText(_translate("Form", "Last Name"))
        self.pushButton_2.setText(_translate("Form", "Back"))
        self.label_3.setText(_translate("Form", "Username"))
        self.label.setText(_translate("Form", "First Name"))
        self.label_5.setText(_translate("Form", "Confirm Password"))
        self.label_8.setText(_translate("Form", "Register Visitor"))
        self.label_14.setText(_translate("Form", "Email"))
        self.pushButton_5.setText(_translate("Form", "Add"))


