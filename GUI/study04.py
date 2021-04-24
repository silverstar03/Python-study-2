import sys
from PySide2.QtWidgets import *
from random import randint

class AnotherWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.count = 0
        self.resize(300, 300)
        layout = QVBoxLayout()
        self.label = QLabel(str(self.count))
        self.plus_button = QPushButton("+")
        layout.addWidget(self.label)
        layout.addWidget(self.plus_button)
        self.setLayout(layout)

        self.plus_button.clicked.connect(self.plus_count)
        # self.plus_button.clicked.connect(self.parent.plus)

    def plus(self, amount):
        if self.isVisihle():
            self.count += amount
            self.label.setText(str(self.count))

    def plus_count(self):  
        self.parent.plus(10)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.count = 0

        qw = QWidget(self)
        layout = QVBoxLayout()
        self.label = QLabel(str(self.count))
        self.show_button = QPushButton("Show Window")
        self.hide_button = QPushButton("Hide Window")
        self.plus_button = QPushButton("+")
        layout.addWidget(self.label)
        layout.addWidget(self.show_button)
        layout.addWidget(self.hide_button)
        layout.addWidget(self.plus_button)
        qw.setLayout(layout)
        self.setCentralWidget(qw)
        self.w = AnotherWindow(self)

        self.show_button.clicked.connect(self.show_window)
        self.hide_button.clicked.connect(self.hide_window)
        self.plus_button.clicked.connect(self.plus_count)

    def plus_count(self):   #창이 안보여도 증가함
        self.w.plus(10)

    def show_window(self):
        geo = self.geometry()
        titlebar_height = QApplication.style().pixelMetric(QStyle.PM_TitleBarHeight)
        self.w.move(geo.x() + 300, geo.y() - titlebar_height)

        self.w.show()

    def hide_window(self):
        self.w.hide()

    def plus(self):
        self.count += 1
        self.label.setText(str(self.count))


if __name__== "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()