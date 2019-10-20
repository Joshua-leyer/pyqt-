import sys 
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

windows = QWidget()
windows.setWindowTitle('你好')
windows.resize(400,400)

label = QLabel(windows)
label.setText('xxx')
windows.show()


sys.exit(app.exec_())