# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout)
from instr import *


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.results()
        self.initUI()
        self.show()
        

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def results(self):
        self.index = (4*(int(self.exp.test1)+ int(self.exp.test2)+int(self.exp.test3))-200)/10
        if int(self.exp.age) >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index<15 and self.index>=11:
                return txt_res2
            elif self.index<11 and self.index>=6:
                return txt_res3
            elif self.index<6 and self.index>=0.5:
                return txt_res4
            elif self.index<0.5:
                return txt_res5
        if int(self.exp.age) <= 14 and int(self.exp.age) >= 13:
            if self.index >= 16.5:
                return txt_res1
            elif self.index<16.5 and self.index>=12.5:
                return txt_res2
            elif self.index<12.5 and self.index>=7.5:
                return txt_res3
            elif self.index<7.5 and self.index>=2:
                return txt_res4
            elif self.index<2:
                return txt_res5
        if int(self.exp.age) <= 12 and int(self.exp.age) >= 11:
            if self.index >= 18:
                return txt_res1
            elif self.index<18 and self.index>=14:
                return txt_res2
            elif self.index<14 and self.index>=9:
                return txt_res3
            elif self.index<9 and self.index>=3.5:
                return txt_res4
            elif self.index<3.5:
                return txt_res5
        if int(self.exp.age) <= 10 and int(self.exp.age) >= 9:
            if self.index >= 19.5:
                return txt_res1
            elif self.index<19.5 and self.index>=15.5:
                return txt_res2
            elif self.index<15.5 and self.index>=10.5:
                return txt_res3
            elif self.index<10.5 and self.index>=5:
                return txt_res4
            elif self.index<5:
                return txt_res5
        if int(self.exp.age) <= 8 and int(self.exp.age) >= 7:
            if self.index >= 21:
                return txt_res1
            elif self.index<21 and self.index>=17:
                return txt_res2
            elif self.index<17 and self.index>=12:
                return txt_res3
            elif self.index<12 and self.index>=6.5:
                return txt_res4
            elif self.index<6.5:
                return txt_res5
    
    def initUI(self):
        self.index_text = QLabel(txt_index + str(self.index))
        self.heart_text  = QLabel(txt_workheart + self.results())

        self.v_line = QVBoxLayout()

        self.v_line.addWidget(self.index_text, alignment =
        Qt.AlignCenter)
        self.v_line.addWidget(self.heart_text, alignment =
        Qt.AlignCenter)
        self.setLayout(self.v_line)
        



