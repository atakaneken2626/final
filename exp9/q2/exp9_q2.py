import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMenu
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):               
        
        exitAct = QAction(QIcon('web.jpg'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        
        editMenu = menubar.addMenu('&Edit')
        
        undo = QMenu('Undo', self)
        undoAct = QAction('Undo Action', self) 
        undo.addAction(undoAct)
        editMenu.addMenu(undo)
        
        redo = QMenu('Redo', self)
        redoAct = QAction('Redo Action', self) 
        redo.addAction(redoAct)
        editMenu.addMenu(redo)
        
        clear = QMenu('Clear', self)
        clearAct = QAction('Clear Action', self) 
        clear.addAction(clearAct)
        editMenu.addMenu(clear)
        
        self.setGeometry(200, 200, 120, 160)
        self.setWindowTitle('First menu application')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())