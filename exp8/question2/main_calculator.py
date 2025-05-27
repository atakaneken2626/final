import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
from functools import partial

# Arayüz ve mantık birleştirildi
class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # Arayüz kurulumunu başlat

        # Hesaplama için değişkenler
        self.flag = 0          # Kullanıcı etkileşim durumunu takip eder (0→ilk sayı, 1→işlem, 2→ikinci sayı, 3→hesapla)
        self.num1 = 0          # İlk sayı
        self.num2 = 0          # İkinci sayı
        self.operator = ""     # Seçilen işlem türü (+, -, *)

    def initUI(self):
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 400, 200)  # Pencere konumu ve boyutu

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Ekran (sonucu gösterecek label)
        self.label = QLabel("0")
        self.label.setFont(QFont("Arial", 18))
        self.label.setStyleSheet("qproperty-alignment: 'AlignRight | AlignVCenter';")
        self.layout.addWidget(self.label, 0, 0, 1, 4)  # 0. satır, 0–3 sütun kaplasın

        # Tuşların yerleşimi
        keys = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
        ]

        # Tüm butonları oluştur ve layout'a yerleştir
        self.buttons = {}
        for key, row, col in keys:
            button = QPushButton(key)
            button.setFixedSize(60, 40)
            button.clicked.connect(partial(self.buttonClicked, key))  # Parametreli fonksiyon bağla
            self.layout.addWidget(button, row, col)
            self.buttons[key] = button

    # Butona tıklandığında yapılacak işlem
    def buttonClicked(self, text):
        if self.flag == 0:  # İlk sayı giriliyorsa
            if text.isdigit():
                self.num1 = int(text)
                self.label.setText(text)
                self.flag = 1  # Operatör bekle

        elif self.flag == 1:  # Operatör girilecekse
            if text in ['+', '-', '*']:
                self.operator = text
                self.label.setText(str(self.num1) + self.operator)
                self.flag = 2  # İkinci sayı bekle

        elif self.flag == 2:  # İkinci sayı giriliyorsa
            if text.isdigit():
                self.num2 = int(text)
                self.flag = 3  # Hesapla

        if self.flag == 3:  # Hesap yapılacaksa
            if self.operator == '+':
                result = self.num1 + self.num2
            elif self.operator == '-':
                result = self.num1 - self.num2
            elif self.operator == '*':
                result = self.num1 * self.num2
            else:
                result = 0

            output = f"{self.num1}{self.operator}{self.num2}={result}"
            self.label.setText(output)
            self.flag = 0  # Sıfırla, yeni işlem için hazır

# Ana uygulama çalıştırma bloğu
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
