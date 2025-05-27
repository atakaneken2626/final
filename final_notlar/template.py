import sys  # Sistem fonksiyonları için sys modülü
from PyQt5.QtWidgets import (  # Gerekli PyQt5 bileşenlerini içe aktar
    QWidget, QLabel, QFormLayout, QMainWindow,
    QApplication, QTabWidget, QLineEdit,
    QHBoxLayout, QCheckBox, QPushButton
)

# Ana pencere sınıfı, QMainWindow’dan türetilmiş
class Example(QMainWindow):
    
    def __init__(self):  # Constructor fonksiyonu
        super().__init__()  # QMainWindow'ın init fonksiyonu çağrılır
        self.initUI()       # Arayüz kurulum fonksiyonu çağrılır
        
    def initUI(self):  # Ana pencerenin arayüzü burada kurulur
        self.setGeometry(300, 300, 280, 170)     # Pencere pozisyonu ve boyutu belirlenir
        self.setWindowTitle('Tab button')       # Başlık çubuğuna yazı eklenir

        self.table_widget = MyTableWidget(self) # Sekmeli yapı oluşturulur ve pencereye eklenir
        self.setCentralWidget(self.table_widget)  # Sekmeler ana pencereye yerleştirilir

        self.show()  # Pencere ekranda gösterilir
        
# Sekmeli pencereyi yöneten sınıf
class MyTableWidget(QWidget):       
     
    def __init__(self, parent):  # Constructor fonksiyonu, parent ana pencere
        super(QWidget, self).__init__(parent)  # QWidget olarak başlatılır
        self.initTabs()  # Sekmeler kurulur
        
    def initTabs(self):  # Sekmeleri başlatan fonksiyon
        self.tabs = QTabWidget()        # QTabWidget → sekme yapısı oluşturulur
        self.tab1 = QWidget()           # İlk sekme
        self.tab2 = QWidget()           # İkinci sekme
        self.tab3 = QWidget()           # Üçüncü sekme
		
        self.tabs.addTab(self.tab1, "Tab 1")  # Sekme 1 eklenir
        self.tabs.addTab(self.tab2, "Tab 2")  # Sekme 2 eklenir
        self.tabs.addTab(self.tab3, "Tab 3")  # Sekme 3 eklenir

        self.tab1UI()  # Sekme 1'in içeriği oluşturulur
        self.tab2UI()  # Sekme 2'nin içeriği oluşturulur
        self.tab3UI()  # Sekme 3'ün içeriği oluşturulur

        layout = QFormLayout()          # Ana layout (form şeklinde)
        layout.addRow(self.tabs)        # Sekmeler layout'a eklenir
        self.setLayout(layout)          # Layout bu widget'e uygulanır
		
    def tab1UI(self):  # Sekme 1 içeriği
        layout = QFormLayout(self)                # Form düzeni kullanılır (label + input)
        layout.addRow("Name", QLineEdit())        # "Name" yazısı ve giriş kutusu
        layout.addRow("Address", QLineEdit())     # "Address" yazısı ve giriş kutusu
        self.tabs.setTabText(0, "Contact Details")  # Sekmenin görünen adı
        self.tab1.setLayout(layout)               # Sekmeye layout atanır
		
    def tab2UI(self):  # Sekme 2 içeriği
        layout = QFormLayout()                    # Form düzeni oluştur
        sex = QHBoxLayout()                       # Cinsiyet seçimi için yatay düzen

        male = QPushButton('Male', self)          # "Male" butonu
        male.setCheckable(True)                   # Tıklanınca seçili kalabilir
        female = QPushButton('Female', self)      # "Female" butonu
        female.setCheckable(True)                 # Aynı şekilde seçilebilir

        sex.addWidget(male)                       # Erkek butonu eklenir
        sex.addWidget(female)                     # Kadın butonu eklenir

        layout.addRow(QLabel("Sex"), sex)         # "Sex" etiketi ile butonlar yan yana konur
        layout.addRow("Date of Birth", QLineEdit())  # Doğum tarihi giriş kutusu

        self.tabs.setTabText(1, "Personal Details")  # Sekmenin görünen adı
        self.tab2.setLayout(layout)               # Sekmeye layout atanır
		
    def tab3UI(self):  # Sekme 3 içeriği
        layout = QHBoxLayout()                    # Yatay düzen oluşturulur

        layout.addWidget(QLabel("subjects"))      # "subjects" etiketi eklenir
        layout.addWidget(QCheckBox("Physics"))    # "Physics" seçeneği
        layout.addWidget(QCheckBox("Maths"))      # "Maths" seçeneği

        self.tabs.setTabText(2, "Education Details")  # Sekmenin görünen adı
        self.tab3.setLayout(layout)               # Sekmeye layout atanır

# Program çalıştırma bloğu
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Uygulama başlatılır
    ex = Example()                # Ana pencere örneği oluşturulur
    sys.exit(app.exec_())         # Uygulama döngüsü başlatılır ve kapanana kadar çalışır
