# ui_calculator.py

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(429, 151)

        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout = QtWidgets.QGridLayout()
        self.buttons = {}

        # Tuşları tanımla
        keys = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3)
        ]

        for key, row, col in keys:
            button = QtWidgets.QPushButton(Form)
            button.setText(key)
            self.gridLayout.addWidget(button, row, col)
            self.buttons[key] = button  # Butonları sakla

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.label.setText(_translate("Form", "0"))
