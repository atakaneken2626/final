from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from q2 import Ui_Form
import sys
import random

class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        self.points = 0
        self.num = None
        self.choice = ""

        # Sinyal bağlantıları burada kuruldu
        self.comboBox.activated[str].connect(self.onActivated)
        self.pushButton_2.clicked.connect(self.buttonClicked)  # Next Number
        self.pushButton.clicked.connect(self.buttonConfirm)    # Confirm

    def onActivated(self, text):
        self.choice = text
        print("Selected:", self.choice)

    def buttonClicked(self):
        self.num = random.randint(1, 5)
        print("Generated number:", self.num)
        self.label.setText(str(self.num))

    def buttonConfirm(self):
        num_to_text = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
        if self.num is not None and self.choice == num_to_text[self.num]:
            self.points += 10
        self.label_2.setText(str(self.points))
        print("Points:", self.points)

# Uygulama başlatma
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
