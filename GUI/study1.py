import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel

# from Pyside2 import QtCore

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1000, 500)
    w.setWindowTitle("Hello Pyside")

    btn = QPushButton('Quit', w)
    btn.move(100,50)   #버튼 위치 정하기
    # btn.clicked.connect(QtCore.QcoreAppliction.instance().quit)
    btn.clicked.connect(lambda : print("cliked!"))


    label = QLabel("Hello", w)
    label.move(100,100)
    label.resize(200,100)


    # label.setGeometry(100,100,200,100) #x,y,w,h
    btn.clicked.connect(lambda : label.setText("World"))


    w.show()

    sys.exit(app.exec_())