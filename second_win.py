# напиши здесь код для второго экрана приложения
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit)
from instr import *
from final_win import *


class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

class TestWin(QWidget):
    
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        else :
            self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

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
        self.text_timer = QLabel("")

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
        Qt.AlignCenter)

        self.v_line2.addWidget(self.text_timer, alignment =
        Qt.AlignCenter)

        self.h_line.addLayout(self.v_line1)
        self.h_line.addLayout(self.v_line2)

        self.setLayout(self.h_line)



    def connects(self):
        self.bnt_next.clicked.connect(self.next_click)
        self.test1.clicked.connect(self.timer_test)
        self.test2.clicked.connect(self.timer_sits)
        self.test3.clicked.connect(self.timer_final)
    
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.hint1age.text(),self.hint1test.text(),
                              self.hint2test.text(),self.hint3test.text())



        self.tw = FinalWin(self.exp)
        
    
    
#app = QApplication([])
#mw = TestWin()
#app.exec_()

