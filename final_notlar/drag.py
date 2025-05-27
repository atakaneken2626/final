from PyQt5.QtWidgets import (QPushButton, QWidget, 
    QLineEdit, QApplication)  # PyQt5'in temel arayüz bileşenlerini içe aktarır
import sys  # Uygulama döngüsünü yönetmek için kullanılır

# Özel buton sınıfı, QPushButton'dan kalıtım alır
class Button(QPushButton):
  
    def __init__(self, title, parent):
        super().__init__(title, parent)   # QPushButton kurucusu çağrılır
        
        self.setAcceptDrops(True)         # Bu buton, sürükle-bırak işlemlerini kabul edebilir

    # Sürüklenen bir nesne buton üzerine girdiğinde bu fonksiyon tetiklenir
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):  # Eğer sürüklenen veri düz metinse
            e.accept()                            # O zaman kabul et
        else:
            e.ignore()                            # Değilse görmezden gel

    # Veri buton üzerine bırakıldığında bu fonksiyon çalışır
    def dropEvent(self, e):
        self.setText(e.mimeData().text())  # Bırakılan metni butonun yazısı yap

# Ana pencere sınıfı
class Example(QWidget):
  
    def __init__(self):
        super().__init__()      # QWidget kurucusu çağrılır
        self.initUI()           # Arayüz kurulumu yapılır
        
    def initUI(self):
        edit = QLineEdit('', self)     # Bir metin giriş kutusu oluşturulur
        edit.setDragEnabled(True)      # Bu kutudan metin sürüklenebilir hale getirilir
        edit.move(30, 65)              # Kutunun pencere üzerindeki konumu

        button = Button("Button", self)  # Özel tanımlı buton oluşturulur
        button.move(190, 65)             # Butonun pencere üzerindeki konumu
        
        self.setWindowTitle('Simple drag and drop')  # Pencere başlığı ayarlanır
        self.setGeometry(300, 300, 300, 150)          # Pencere boyutu ve ekran üzerindeki konumu

# Uygulamanın çalıştığı ana blok
if __name__ == '__main__':
    app = QApplication(sys.argv)  # PyQt5 uygulaması başlatılır
    ex = Example()                # Ana pencere örneği oluşturulur
    ex.show()                     # Pencere ekranda gösterilir
    app.exec_()                   # Olay döngüsü başlatılır
