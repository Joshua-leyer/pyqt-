import sys
from PyQt5.QtWidgets import *



# 4 --------弹出信息提示窗口

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.iniUI()
    def iniUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('message box')
        self.show()
    def closeEvent(self,event):
        reply = QMessageBox.question(self,'message',"Are you sure to quit ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if replay == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())