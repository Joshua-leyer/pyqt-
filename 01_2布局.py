import sys
from PyQt5.QtWidgets import *

class Exapmle(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
    def Init_UI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('学点编程')

        btn1 = QPushButton('剪刀',self)
        btn2 = QPushButton('石头',self)
        btn3 = QPushButton('布',self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Exapmle()
    app.exit(app.exec_())