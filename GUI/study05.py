import sys, random
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore
from random import randint

class MyCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.count = 0
        self.smile = QImage("smile.png")
        self.font = QFont('Decorative', 36)

        self.timer = QtCore.QTimer()
        #타이머 터지는 주기 설정
        self.timer.setInterval(1000)
        # timeout 시그널 연결
        self.timer.timeout.connect(self.doTimerJob)
        # 타이머 시작
        self.timer.start()

    def doTimerJob(self):
        self.update()

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Right : print("RIGHT")
        elif key == QtCore.Qt.Key_Left : print("LEFT")
        elif key == QtCore.Qt.Key_Down : print("DOWN")
        elif key == QtCore.Qt.Key_Up : print("UP")

    def mousePressEvent(self, event):
        pos = event.pos()
        #event.globalPos()를 사용하면 자신의 컴퓨터 크기에 맞는 픽셀이 나옴
        self.x = pos.x()
        self.y = pos.y()
        print(self.x, self.y)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        x = randint(0, 500 - 50)
        y = randint(0, 500 - 50)

        qp.setFont(self.font)
        qp.drawText(QtCore.QRect(0, 0, 500, 500),
                    QtCore.Qt.AlignCenter, f"{self.count}")
        qp.drawImage(QtCore.QRect(x, y, 50, 50), self.smile)
        self.count += 1

        qp.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    c = MyCanvas()
    c.show()

    sys.exit(app.exec_())