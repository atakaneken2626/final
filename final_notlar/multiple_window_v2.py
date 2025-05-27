import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt

# Ana pencere arayüz sınıfı
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")            # Pencere tanımlaması
        MainWindow.resize(292, 264)                        # Pencere boyutu
        self.centralwidget = QtWidgets.QWidget(MainWindow) # Ortadaki widget
        self.centralwidget.setObjectName("centralwidget")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)    # Checkbox oluşturuluyor
        self.checkBox.setGeometry(QtCore.QRect(70, 50, 251, 141))  # Konum ve boyut
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setChecked(False)                             # Başlangıçta işaretli değil

        MainWindow.setCentralWidget(self.centralwidget)            # Ortadaki widget'ı ata

        self.menubar = QtWidgets.QMenuBar(MainWindow)              # Menü çubuğu
        self.menubar.setGeometry(QtCore.QRect(0, 0, 292, 21))      
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)          # Durum çubuğu
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.w = None                                  # Yeni pencere henüz oluşturulmadı
        self.checkBox.stateChanged.connect(self.show_new_window)  # Checkbox değişince pencereyi göster
        MainWindow.setCentralWidget(self.checkBox)     # Checkbox ana içerik olarak yerleştirildi

        self.retranslateUi(MainWindow)                 # Metinleri çevir (başlık vb.)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) # Otomatik bağlantı (fancy Qt özelliği)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow")) # Başlık
        self.checkBox.setText(_translate("MainWindow", "Checked for new window")) # Checkbox yazısı

    def show_new_window(self, state):  # Checkbox işaretlenirse çağrılan fonksiyon
        if state == Qt.Checked:        # Eğer işaretlendiyse
            if self.w is None:         # Ve pencere daha önce oluşturulmadıysa
                self.FormWindow = QtWidgets.QWidget() # Yeni boş pencere oluştur
                self.w = Ui_Form()     # Form sınıfını başlat
                self.w.setupUi(self.FormWindow) # Form arayüzünü pencereye kur
            self.FormWindow.show()     # Pencereyi göster


# İkinci pencere arayüz sınıfı
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")              # Form ayarı
        Form.resize(400, 300)                   # Boyut ayarı

        self.label = QtWidgets.QLabel(Form)     # Label oluşturuluyor
        self.label.setGeometry(QtCore.QRect(110, 90, 111, 91))  # Etiket konumu
        self.label.setObjectName("label")

        self.retranslateUi(Form)                # Metin çeviri işlemleri
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))   # Form başlığı
        self.label.setText(_translate("Form", "New Window"))  # Etiket yazısı


# Uygulamayı çalıştıran sınıf
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()        # Ana pencere başlat
        self.ui = Ui_MainWindow()               # Arayüz sınıfını çağır
        self.ui.setupUi(self)                   # Arayüzü pencereye uygula


# Ana uygulama bloğu
if __name__ == '__main__':
    app = QtWidgets.QApplication([])        # Uygulama başlatılıyor
    ex = mywindow()                         # Ana pencere oluşturuluyor
    ex.show()                               # Gösteriliyor
    sys.exit(app.exec_())                   # Uygulama döngüsü çalışıyor
