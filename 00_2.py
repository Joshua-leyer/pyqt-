#初步认识
# 尝试写一个windows窗口

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

'''
if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('first one')
    w.show()

    sys.exit(app.exec_())
'''



'''
#2 -------结合命令行，自定义窗口标题。
# 需要了解 sys.argv  用法。这个教程没讲，我另外搜索的，不知道为什么，我看到这样的教程很气。见多了。越看越累，最失望的是，你看了半天发现这个教程什么都没写。
# 学了个p。。。

if __name__ == '__main__':
    app = QApplication(sys.argv)
    try:
        if len(sys.argv) < 2:
            raise ValueError
        else:
            title = "".join(sys.argv[1:])
    except ValueError:
        title = " "
    
    w = QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle(title)
    w.show()

    sys.exit(app.exec_())

'''

# 3 --------尝试添加一个窗口图标
# 4 ------------尝试增加一个关闭按钮，实现关闭功能。

class Ico(QWidget):
    def __init__(self):
        super().__init__()
        self.iniUI()
        
    def iniUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('tree one')
        self.setWindowIcon(QIcon('./sources/favicon_star.png'))

        qbth = QPushButton('quit',self)
        qbth.clicked.connect(QCoreApplication.instance().quit)
        qbth.resize(70,30)
        qbth.move(50,50)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())



'''
 我不是很明白super()，为什么要试着,self.iniUI().
 ???????????????????????????????????????
'''

