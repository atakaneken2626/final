# -*- coding: utf-8 -*- 
# Dosya UTF-8 karakter setini kullanıyor (Türkçe karakter desteği sağlar)

# Bu dosya, Qt Designer'da oluşturulup pyuic5 aracıyla dönüştürülmüştür.
# Elle değişiklik yapmak tavsiye edilmez, çünkü pyuic5 ile yeniden çevrildiğinde silinir.

from PyQt5 import QtCore, QtGui, QtWidgets  # PyQt5’in temel modülleri içe aktarılıyor

# Ui_MainWindow sınıfı, Designer'da tanımlanan arayüzü oluşturur
class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):  # Bu fonksiyon, arayüzü pencereye yerleştirir
        MainWindow.setObjectName("MainWindow")       # Pencerenin nesne adı
        MainWindow.resize(292, 264)                  # Pencere boyutu ayarlanıyor

        self.centralwidget = QtWidgets.QWidget(MainWindow)  # Ana içerik alanı (orta bölge)
        self.centralwidget.setObjectName("centralwidget")   # Nesne adı atanıyor

        # Checkbox oluşturuluyor ve konumlandırılıyor
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)  # Checkbox, central widget üzerine yerleştirilir
        self.checkBox.setGeometry(QtCore.QRect(70, 50, 251, 141))  # X=70, Y=50, genişlik=251, yükseklik=141
        self.checkBox.setObjectName("checkBox")                   # Nesne adı atanıyor (koddan erişmek için)

        MainWindow.setCentralWidget(self.centralwidget)  # centralwidget, ana pencereye yerleştirilir

        self.menubar = QtWidgets.QMenuBar(MainWindow)     # Menü çubuğu ekleniyor
        self.menubar.setGeometry(QtCore.QRect(0, 0, 292, 21))  # Menü çubuğu boyutu ve konumu
        self.menubar.setObjectName("menubar")             # Menü çubuğuna nesne adı veriliyor
        MainWindow.setMenuBar(self.menubar)               # Menü çubuğu ana pencereye ekleniyor

        self.statusbar = QtWidgets.QStatusBar(MainWindow)  # Durum çubuğu oluşturuluyor
        self.statusbar.setObjectName("statusbar")          # Nesne adı veriliyor
        MainWindow.setStatusBar(self.statusbar)            # Ana pencereye durum çubuğu ekleniyor

        self.retranslateUi(MainWindow)  # Yazılar ve metin içerikleri ayrı fonksiyonda tanımlanır
        QtCore.QMetaObject.connectSlotsByName(MainWindow)  # Qt sinyal-slot sistemini otomatik eşleştirir

    def retranslateUi(self, MainWindow):  # Metin içeriklerini tanımlar
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))  # Pencere başlığı
        self.checkBox.setText(_translate("MainWindow", "Checked for new window"))  # Checkbox üzerindeki yazı
