# main.py

from PyQt5 import QtWidgets
from finalw2 import Ui_Form  # Arayüz dosyanın ismi finalw2.py olacak
import sys

class PrimeApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Buton bağlantısı
        self.pushButton_run.clicked.connect(self.run_clicked)

    def run_clicked(self):
        try:
            n = int(self.lineEdit_number.text())  # sayıyı al
            primes = self.calculate_primes(n)

            if self.comboBox.currentText() == "Print the text box":
                self.print_text_box(primes)
                self.label_status.setText("Printing the text box")
            else:
                self.print_file(primes)
                self.label_status.setText("Writing the file")

        except:
            self.label_status.setText("ERROR: input must be valid number")

    def calculate_primes(self, n):
        primes = []
        for num in range(2, n + 1):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
        return primes

    def print_text_box(self, prime_list):
        self.textEdit_asal.clear()
        self.textEdit_asal.append(" ".join(map(str, prime_list)))

    def print_file(self, prime_list):
        with open("prime_numbers.txt", "w") as f:
            for p in prime_list:
                f.write(str(p) + "\n")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PrimeApp()
    window.show()
    sys.exit(app.exec_())
