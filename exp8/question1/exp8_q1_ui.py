# ui_rgb_slider.py

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setWindowTitle("RGB Color Picker")
        Form.setAutoFillBackground(True)

        # Renk gösterim çerçevesi
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 20, 301, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Label sütunu (R, G, B)
        self.widget_labels = QtWidgets.QWidget(Form)
        self.widget_labels.setGeometry(QtCore.QRect(10, 120, 77, 81))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_labels)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_labels = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("R:")
        self.label_2 = QtWidgets.QLabel("G:")
        self.label_3 = QtWidgets.QLabel("B:")
        self.verticalLayout_labels.addWidget(self.label)
        self.verticalLayout_labels.addWidget(self.label_2)
        self.verticalLayout_labels.addWidget(self.label_3)

        self.verticalLayout_values = QtWidgets.QVBoxLayout()
        self.label_5 = QtWidgets.QLabel("0")  # R değeri
        self.label_4 = QtWidgets.QLabel("0")  # G değeri
        self.label_6 = QtWidgets.QLabel("0")  # B değeri
        self.verticalLayout_values.addWidget(self.label_5)
        self.verticalLayout_values.addWidget(self.label_4)
        self.verticalLayout_values.addWidget(self.label_6)

        self.horizontalLayout.addLayout(self.verticalLayout_labels)
        self.horizontalLayout.addLayout(self.verticalLayout_values)

        # Slider sütunu (R, G, B)
        self.widget_sliders = QtWidgets.QWidget(Form)
        self.widget_sliders.setGeometry(QtCore.QRect(90, 120, 211, 80))
        self.verticalLayout_sliders = QtWidgets.QVBoxLayout(self.widget_sliders)
        self.verticalLayout_sliders.setContentsMargins(0, 0, 0, 0)

        self.horizontalSlider = QtWidgets.QSlider()
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalSlider_2 = QtWidgets.QSlider()
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalSlider_3 = QtWidgets.QSlider()
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)

        self.verticalLayout_sliders.addWidget(self.horizontalSlider)
        self.verticalLayout_sliders.addWidget(self.horizontalSlider_2)
        self.verticalLayout_sliders.addWidget(self.horizontalSlider_3)

        # Varsayılan renk nesnesi
        self.col = QtGui.QColor(0, 0, 0)

        # Slot bağlantıları dışarıdan bağlanacaktır (main dosyasında)
        QtCore.QMetaObject.connectSlotsByName(Form)
