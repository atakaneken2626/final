# -*- coding: utf-8 -*-
"""
Progress Bar (İlerleme Çubuğu) örneği.
@author: burak
"""

from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication)  # Gerekli widgetlar
from PyQt5.QtCore import QBasicTimer  # Timer kullanılmak üzere içe aktarılmış ama kodda kullanılmıyor
import sys  # Sistemden uygulamayı başlatmak için

# Ana pencere sınıfı
class Example(QWidget):
    
    def __init__(self):
        super().__init__()  # QWidget başlat
        self.initUI()       # Arayüzü oluştur
        
    def initUI(self):  # Arayüz tanımları
        self.pbar = QProgressBar(self)                # İlerleme çubuğu oluştur
        self.pbar.setGeometry(30, 40, 200, 25)        # Konum ve boyut

        self.btn = QPushButton('Start', self)         # Başlat butonu oluştur
        self.btn.move(40, 80)                         # Butonun konumu
        self.btn.clicked.connect(self.doAction)       # Tıklanırsa doAction fonksiyonu çalışır

        self.step = 0                                 # İlerlemenin sayacı
        self.setGeometry(300, 300, 280, 170)          # Ana pencere boyut ve konumu
        self.setWindowTitle('QProgressBar')           # Pencere başlığı
        self.show()                                   # Pencereyi göster
        
    def doAction(self):
        # Bu fonksiyon çalıştığında çok büyük bir döngü başlar
        # Ancak bu döngü **UI'yi kilitler**, çünkü zamanlayıcı (timer) kullanılmamış

        for i in range(0, 1000000000000):             # Aşırı büyük bir döngü (uygulamayı dondurur)
            if i % 1000000 == 0:                      # Her milyon adımda bir
                self.step = self.step + 1             # İlerleme değeri artırılır
                self.pbar.setValue(self.step)         # İlerleme çubuğu güncellenir
            
            if self.step >= 100:                      # %100'e ulaşıldığında
                self.btn.setText('Finished')          # Butonun metni değişir
