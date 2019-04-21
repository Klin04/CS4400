# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdministratorManageSite.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(667, 480)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 60, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 181, 17))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(130, 60, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(450, 60, 86, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(370, 60, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(176, 100, 151, 20))
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(340, 100, 86, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 140, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 140, 89, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 140, 89, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 140, 89, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 400, 89, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(70, 200, 551, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Site"))
        self.label_2.setText(_translate("Form", "Manage Site"))
        self.label_3.setText(_translate("Form", "Manager"))
        self.label_4.setText(_translate("Form", "Open Everyday"))
        self.pushButton.setText(_translate("Form", "Filter"))
        self.pushButton_2.setText(_translate("Form", "Create"))
        self.pushButton_3.setText(_translate("Form", "Edit"))
        self.pushButton_4.setText(_translate("Form", "Delete"))
        self.pushButton_5.setText(_translate("Form", "Back"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Manager"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Open Everyday"))

