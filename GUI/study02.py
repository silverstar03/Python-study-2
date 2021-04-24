import sys
from PySide2.QtWidgets import QApplication, QLabel, QWidget, \
    QPushButton, QMainWindow, QCheckBox, QSlider, QLineEdit
from PySide2 import QtCore, QtGui

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        self.demoWidget()

    def changed(self, state): #state부분은 다른 이름으로 바꿔도 됨
        # print(state)
        print("Checked" if state == QtCore.Qt.Checked else "Unchecked")
        #그냥 2로 적는것보단 QtCore의 Qt라는 페키지에 있는 것을 사용하는 것이 더 좋음

    def slider(self, state):
        print(state)
        self.label.setText(str(state))

    def calculation_add(self):
        num1 = int(self.qle1.text())
        num2 = int(self.qle2.text())
        self.result.setText(str(num1+num2))

    def demoWidget(self):
        cb = QCheckBox("MyCheckBox", self)
        cb.move(0, 0)
        cb.resize(cb.sizeHint()) #가장 최적의 사이즈를 찾아줌
        cb.stateChanged.connect(self.changed)
        #stateChanged는 시그널임. self.changed

        s = QSlider(QtCore.Qt.Horizontal , self)
        s.move(30,30)
        s.setRange(0,100) #범위 지정
        s.resize(300,10)
        s.setSingleStep(2) #최소 단위 설정
        s.valueChanged.connect(self.slider)

        self.label = QLabel(self)
        self.label.move(0, 100)
        self.label.setText("Hello <b style='color: red'>QLabel</b>")

        self.qle1 = QLineEdit(self)
        self.qle2 = QLineEdit(self)
        label2 = QLabel(self)

        self.qle1.move(0,150)
        label2.move(110,150)
        label2.setText("+")
        label2.resize(20,30)
        self.qle2.move(130,150)

        self.button = QPushButton("result", self)
        self.button.move(0,200)
        self.button.clicked.connect(self.calculation_add)

        self.result = QLabel(self)
        self.result.move(0,250)
        self.result.setFont(QtGui.QFont('SansSerif', 20))

if __name__== "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    sys.exit(app.exec_())