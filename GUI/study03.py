import sys
from PySide2.QtWidgets import QApplication, QLabel, QWidget, \
    QPushButton, QMainWindow, QCheckBox, QSlider, QLineEdit, \
    QDialog, QDialogButtonBox, QVBoxLayout
from PySide2 import QtCore, QtGui

# QDialog는 위젯이라고 생각하면 된다. 새 창을 띄워줌
class CustomDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        msg = QLabel("Hello Dialog")
        self.layout.addWidget(msg)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)

        button = QPushButton("press me for a dialog!", self)
        button.clicked.connect(self.button_clicked)
        button.resize(button.sizeHint())

        self.dlg = CustomDialog()

    def button_clicked(self, s):

        self.dlg.show()
        """
        dlg = CustomDialog()
        ret = dlg.exec_()
        print(ret)
        if ret == QDialog.Accepted: print("accepted")
        elif ret == QDialog.Rejected: print("rejected")
        """


if __name__== "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    sys.exit(app.exec_())