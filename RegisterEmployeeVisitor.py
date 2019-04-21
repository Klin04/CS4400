# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterEmployeeVisitor.ui'
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
        Form.resize(927, 451)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(210, 80, 81, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 80, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 410, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(430, 270, 61, 17))
        self.label_12.setObjectName("label_12")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(560, 130, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(470, 80, 81, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(210, 180, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(590, 270, 131, 17))
        self.label_13.setObjectName("label_13")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(560, 80, 113, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(280, 230, 171, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(560, 230, 221, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_11 = QtWidgets.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(660, 270, 101, 25))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 130, 113, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(200, 270, 67, 17))
        self.label_11.setObjectName("label_11")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(480, 270, 86, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(210, 230, 67, 17))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(210, 130, 71, 17))
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(490, 230, 131, 17))
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(260, 270, 141, 25))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(490, 180, 131, 17))
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(630, 180, 171, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(390, 10, 251, 61))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 410, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(470, 130, 67, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 180, 171, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(190, 310, 67, 17))
        self.label_14.setObjectName("label_14")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 410, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.addEmail)

        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)

        self.widget = QtWidgets.QScrollArea(Form)
        self.widget.setGeometry(QtCore.QRect(250, 300, 521, 101))
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
        self.label_3.setText(_translate("Form", "First Name"))
        self.pushButton_3.setText(_translate("Form", "Register"))
        self.label_12.setText(_translate("Form", "State"))
        self.label_4.setText(_translate("Form", "Last Name"))
        self.label_5.setText(_translate("Form", "Password"))
        self.label_13.setText(_translate("Form", "Zipcode"))
        self.label_11.setText(_translate("Form", "City"))
        self.label_7.setText(_translate("Form", "Phone"))
        self.label_6.setText(_translate("Form", "Username"))
        self.label_10.setText(_translate("Form", "Address"))
        self.label_8.setText(_translate("Form", "Confirm Password"))
        self.label.setText(_translate("Form", "Register Employee-Visitor"))
        self.pushButton_2.setText(_translate("Form", "Back"))
        self.label_2.setText(_translate("Form", "User Type"))
        self.pushButton_4.setText(_translate("Form", "Add"))
        self.label_14.setText(_translate("Form", "Email"))


