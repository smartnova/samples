#!/usr/bin/env python

import sys
from PyQt5 import QtSvg, QtWidgets
from PyQt5.QtGui import QPainter

class SVG(QtWidgets.QWidget):
    def __init__(self, path):
        self.path = path
        app = QtWidgets.QApplication(sys.argv)

        super().__init__()
        self.init_ui()
        self.show()

        app.exec_()

    def init_ui(self):
        self.resize(500, 500)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        QtSvg.QSvgRenderer(self.path).render(painter)

if __name__ == '__main__':
    SVG(sys.argv[1])
