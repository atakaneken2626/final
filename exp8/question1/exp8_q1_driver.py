# main_rgb_slider.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor
from exp8_q1_ui import Ui_Form  # arayüz dosyasını import ediyoruz


class RGBSliderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.col = QColor(0, 0, 0)

        # Slider value değişince arayüzdeki değer güncellensin
        self.ui.horizontalSlider.valueChanged['int'].connect(self.ui.label_5.setNum)
        self.ui.horizontalSlider_2.valueChanged['int'].connect(self.ui.label_4.setNum)
        self.ui.horizontalSlider_3.valueChanged['int'].connect(self.ui.label_6.setNum)

        # Slider değişince arka plan rengi değişsin
        self.ui.horizontalSlider.valueChanged.connect(self.update_color)
        self.ui.horizontalSlider_2.valueChanged.connect(self.update_color)
        self.ui.horizontalSlider_3.valueChanged.connect(self.update_color)

    def update_color(self):
        valR = self.ui.horizontalSlider.value()
        valG = self.ui.horizontalSlider_2.value()
        valB = self.ui.horizontalSlider_3.value()

        self.col.setRgb(valR, valG, valB)
        self.ui.frame.setStyleSheet(f"QFrame {{ background-color: {self.col.name()} }}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RGBSliderApp()
    window.show()
    sys.exit(app.exec_())
