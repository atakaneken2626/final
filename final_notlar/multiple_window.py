import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

# Ana pencere sınıfı
class App(QMainWindow):

    def __init__(self):
        super().__init__()              # QMainWindow constructor'ını çağır
        self.initUI()                   # Arayüzü kur

    def initUI(self):
        self.w = None                   # Yeni pencere henüz oluşturulmadı

        self.setGeometry(300, 300, 280, 170)     # Ana pencere konumu ve boyutu
        self.setWindowTitle('Main Window')      # Başlık ayarlanıyor

        self.button = QPushButton("Push for Window")        # Buton oluşturuluyor
        self.button.clicked.connect(self.show_new_window)   # Butona tıklanma olayına fonksiyon bağlanıyor
        self.setCentralWidget(self.button)                  # Buton, pencerenin ortasına yerleştiriliyor

        self.show()                           # Ana pencereyi göster

    def show_new_window(self, checked):
        if self.w is None:                    # Eğer pencere daha önce oluşturulmadıysa
            self.w = AnotherWindow()          # Yeni pencere nesnesi oluştur
        self.w.show()                         # Yeni pencereyi göster


# Açılacak ikinci pencere sınıfı
class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()                    # QWidget constructor
        layout = QVBoxLayout()                # Dikey yerleşim oluştur
        self.label = QLabel("Another Window") # Etiket oluştur
        layout.addWidget(self.label)          # Etiketi yerleşime ekle
        self.setLayout(layout)                # Pencereye yerleşimi ata


# Uygulama başlatma
if __name__ == '__main__':
    app = QApplication(sys.argv)      # PyQt5 uygulaması başlatılıyor
    ex = App()                        # Ana pencere sınıfı çağrılıyor
    sys.exit(app.exec_())             # Uygulama döngüsü başlatılıyor

