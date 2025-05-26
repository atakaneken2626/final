# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1a_v2.ui'
# Created by: PyQt5 UI code generator 5.6

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(563, 392)
        font = QtGui.QFont()
        font.setUnderline(False)
        Form.setFont(font)

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 180, 51, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(230, 180, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Red", "Green", "Blue", "Black"])

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 160, 47, 13))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(240, 160, 47, 13))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(220, 70, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(140, 260, 70, 17))
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(210, 260, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(260, 260, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(340, 260, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Update Text"))
        self.label.setText(_translate("Form", "Size"))
        self.label_3.setText(_translate("Form", "Color"))
        self.label_4.setText(_translate("Form", "Python"))
        self.checkBox.setText(_translate("Form", "Bold"))
        self.checkBox_2.setText(_translate("Form", "Italic"))
        self.checkBox_3.setText(_translate("Form", "Underline"))
        self.checkBox_4.setText(_translate("Form", "Strikeout"))
