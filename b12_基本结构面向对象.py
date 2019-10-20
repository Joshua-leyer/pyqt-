import sys 
from PyQt5.QtWidgets import *

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Qlabel study')
        self.resize(300,300)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText('xxx')
        label.resize(50,150)

app = QApplication(sys.argv)
window = Windows()
window.show()
sys.exit(app.exec_())