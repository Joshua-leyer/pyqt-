import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('事件与信号')
        self.lab = QLabel('方向',self)
        self.lab.setGeometry(150,100,50,50)
        self.show()
    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Up:
            self.lab.setText('↑')
        elif e.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif e.key() == Qt.Key_Left:
            self.lab.setText('←')
        elif e.key() == Qt.Key_Right:
            self.lab.setText('→')

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
'''
我刚看 没懂为什么，他是怎么获取到用户输入的键盘事件的，我没看到运行keyPressEvent函数。。
我就猜是自动运行的，可能是运行实例的时候自动就运行个段函数了。真服了。学个东西，都靠猜。
我关键词搜索这个函数的名字，在知乎的某个回答里看到。那个问题的回答只有两个人。。。有个人说，
此函数是通过继承而来的虚函数（又一个新名词，我快郁闷死）。最后说，不需要调用，而且只在当前重写的类中生效。
你看看我找的教程里面，就是一堆代码给你，自己抄去吧，能运行就算运气好的。也不讲讲为什么。。。