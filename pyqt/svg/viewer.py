#!/usr/bin/env python

import sys
from PyQt5 import QtSvg, QtWidgets
from PyQt5.QtGui import QPainter

class SVG(QtWidgets.QWidget):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)

        super().__init__()
        self.init_ui()
        self.show()

        app.exec_()

    def init_ui(self):
        self.resize(500, 500)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        QtSvg.QSvgRenderer(sys.argv[1]).render(painter)

SVG()
