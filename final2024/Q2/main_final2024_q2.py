import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from final2024_q2 import Ui_Form  # .ui'den dönüştürülmüş arayüz dosyan

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Başlangıçta butonlar ve combo box devre dışı
        self.disable_operations()

        # Event bağlantıları
        self.ui.pushButton_generatenumbers.clicked.connect(self.generate_numbers)
        self.ui.radioButton_max.toggled.connect(self.handle_operation)
        self.ui.radioButton_min.toggled.connect(self.handle_operation)
        self.ui.radioButton_reverse.toggled.connect(self.handle_operation)
        self.ui.radioButton_sort.toggled.connect(self.sort_selected)
        self.ui.comboBox.currentIndexChanged.connect(self.apply_sort_option)

        # Liste
        self.numbers = []

    def disable_operations(self):
        self.ui.radioButton_max.setEnabled(False)
        self.ui.radioButton_min.setEnabled(False)
        self.ui.radioButton_sort.setEnabled(False)
        self.ui.radioButton_reverse.setEnabled(False)
        self.ui.comboBox.setEnabled(False)

    def enable_operations(self):
        self.ui.radioButton_max.setEnabled(True)
        self.ui.radioButton_min.setEnabled(True)
        self.ui.radioButton_sort.setEnabled(True)
        self.ui.radioButton_reverse.setEnabled(True)

    def generate_numbers(self):
        self.numbers = [random.randint(0, 100) for _ in range(40)]
        self.ui.textEdit_number.setText(", ".join(map(str, self.numbers)))
        self.ui.label_status.setText("Numbers are generated")
        self.enable_operations()

    def handle_operation(self):
        if not self.numbers:
            return

        if self.ui.radioButton_max.isChecked():
            result = max(self.numbers)
            self.ui.textEdit_result.setText(str(result))
            self.ui.label_status.setText("Maximum number is determined")
            self.ui.comboBox.setEnabled(False)

        elif self.ui.radioButton_min.isChecked():
            result = min(self.numbers)
            self.ui.textEdit_result.setText(str(result))
            self.ui.label_status.setText("Minimum number is determined")
            self.ui.comboBox.setEnabled(False)

        elif self.ui.radioButton_reverse.isChecked():
            result = list(reversed(self.numbers))
            self.ui.textEdit_result.setText(", ".join(map(str, result)))
            self.ui.label_status.setText("Numbers are reversed")
            self.ui.comboBox.setEnabled(False)

    def sort_selected(self):
        if self.ui.radioButton_sort.isChecked():
            self.ui.comboBox.setEnabled(True)
        else:
            self.ui.comboBox.setEnabled(False)

    def apply_sort_option(self):
        if not self.numbers or not self.ui.radioButton_sort.isChecked():
            return

        option = self.ui.comboBox.currentText()

        if option == "Ascending":
            result = sorted(self.numbers)
            self.ui.textEdit_result.setText(", ".join(map(str, result)))
            self.ui.label_status.setText("Numbers are sorted in ascending order")

        elif option == "Descending":
            result = sorted(self.numbers, reverse=True)
            self.ui.textEdit_result.setText(", ".join(map(str, result)))
            self.ui.label_status.setText("Numbers are sorted in descending order")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
