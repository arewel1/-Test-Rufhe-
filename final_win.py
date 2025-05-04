# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout)
from instr import *


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):
        self.index = QLabel(txt_index)
        self.heart  = QLabel(txt_workheart)

        self.v_line = QVBoxLayout()

        self.v_line.addWidget(self.index)
        self.v_line.addWidget(self.heart)
        



