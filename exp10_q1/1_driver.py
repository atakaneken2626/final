from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from q1 import Ui_Form
import sys

class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        # Başlangıç font özellikleri
        self.flagBold = False
        self.flagItalic = False
        self.flagUnderline = False
        self.flagStrikeout = False
        self.font_size = 20
        self.Color = "Black"

        # Bağlantılar
        self.lineEdit.textChanged[str].connect(self.onChanged)
        self.comboBox.activated[str].connect(self.onActivated)
        self.pushButton.clicked.connect(self.buttonClicked)
        self.checkBox.stateChanged.connect(self.changeBold)
        self.checkBox_2.stateChanged.connect(self.changeItalic)
        self.checkBox_3.stateChanged.connect(self.changeUnderline)
        self.checkBox_4.stateChanged.connect(self.changeStrikeout)

    def onChanged(self, text):
        try:
            self.font_size = int(text)
        except ValueError:
            self.font_size = 20  # default size
        print("Font size:", self.font_size)

    def onActivated(self, text):
        self.Color = text
        print("Color selected:", self.Color)

    def changeBold(self, state):
        self.flagBold = (state == Qt.Checked)

    def changeItalic(self, state):
        self.flagItalic = (state == Qt.Checked)

    def changeUnderline(self, state):
        self.flagUnderline = (state == Qt.Checked)

    def changeStrikeout(self, state):
        self.flagStrikeout = (state == Qt.Checked)

    def buttonClicked(self):
        # Renk ayarı
        color_style = f"color: {self.Color.lower()}"
        self.label_4.setStyleSheet(color_style)

        # Font ayarı
        font = QtGui.QFont()
        font.setPointSize(self.font_size)
        font.setBold(self.flagBold)
        font.setItalic(self.flagItalic)
        font.setUnderline(self.flagUnderline)
        font.setStrikeOut(self.flagStrikeout)
        self.label_4.setFont(font)

# Uygulama başlatma
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
