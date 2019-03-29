import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__() 
        self.title = "Jogo danin"
        self.left = 10
        self.right = 10
        self.width = 600
        self.height = 800
        self.initUI()

    def initUI(self):
       self.setWindowTitle(self.title)
       self.setGeometry(self.left, self.top, self.width, self.height)
       self.show()

sys.exit(QApplication(sys.argv))

