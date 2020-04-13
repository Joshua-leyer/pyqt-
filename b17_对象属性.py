import sys
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('测试继承')
        self.resize(400,400)
        self.setup_ui()

    def setup_ui(self):
        self.ObjectInherited()

    def ObjectInherited(self):
        mros = QObject.mro()
        for mro in mros:
            print(mro)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
