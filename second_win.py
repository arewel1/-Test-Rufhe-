# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit)
from instr import *
from final_win import *

class TestWin(QWidget):
    
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move( win_x, win_y)
    
    def initUI(self):
        self.name = QLabel(txt_name)
        self.age  = QLabel(txt_age)
        self.back = QLabel(txt_test1)
        self.squats = QLabel(txt_test2)
        self.pulse = QLabel(txt_test3)
        self.time = QLabel("dsad")

        self.test1 = QPushButton(txt_starttest1)
        self.test2 = QPushButton(txt_starttest2)
        self.test3 = QPushButton(txt_starttest3)
        self.bnt_next = QPushButton(txt_sendresults)

        self.hint1name = QLineEdit(txt_hintname)
        self.hint1age = QLineEdit(txt_hintage)
        self.hint1test = QLineEdit(txt_hinttest1)
        self.hint2test = QLineEdit(txt_hinttest2)
        self.hint3test = QLineEdit(txt_hinttest3)

        self.h_line = QHBoxLayout()
        self.v_line1 = QVBoxLayout()
        self.v_line2 = QVBoxLayout()

        self.v_line1.addWidget(self.name, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.hint1name, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.age, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.hint1age, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.back, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.test1, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.hint1test, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.squats, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.test2, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.pulse, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.test3, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.hint2test, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.hint3test, alignment =
        Qt.AlignLeft)
        self.v_line1.addWidget(self.bnt_next, alignment =
        Qt.AlignRight)

        self.v_line2.addWidget(self.time, alignment =
        Qt.AlignRight)

        self.h_line.addLayout(self.v_line1)
        self.h_line.addLayout(self.v_line2)

        self.setLayout(self.h_line)



    def connects(self):
        self.bnt_next.clicked.connect(self.next_click)
    
    def next_click(self):
        self.hide()
        self.tw = FinalWin()
    
    
app = QApplication([])
mw = TestWin()

app.exec_()

