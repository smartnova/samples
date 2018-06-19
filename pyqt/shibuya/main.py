#!/usr/bin/env python

import sys

import scipy

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

# Constants

BLACK = QtGui.QColor('black')
WHITE = QtGui.QColor('white')
G_FONT = QtGui.QFont('Times New Roman', 16, 75)
PEN = QtGui.QPen(BLACK)
BLACK_BRUSH = QtGui.QBrush(BLACK, Qt.SolidPattern)
WHITE_BRUSH = QtGui.QBrush(WHITE, Qt.SolidPattern)
DASH_PEN = QtGui.QPen(BLACK_BRUSH, 1, Qt.DashLine)
DOT_PEN = QtGui.QPen(BLACK_BRUSH, 1, Qt.DotLine)

# Window

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
uic.loadUi('view.ui', window)
with open('view.css', 'r') as css:
    app.setStyleSheet(css.read().replace('\n', ''))

def altitude_list():
    model = QtCore.QStringListModel(
        [str(a) for a in [0, 25, 50, 75, 100,
                          150, 200, 250,
                          300, 400, 500, 600, 700]])
    window.altitudeList.setModel(model)

# Data items

f = scipy.vectorize(lambda t: (t - 120) * (t - 120) / 120)
g = scipy.vectorize(lambda t: (t - 160) * (t - 160) / 120 - 300)

ts = scipy.random.randint(120, 300, 10)
xs = f(ts) + (scipy.random.randn(len(ts)) - 0.5) * 3
ys = g(ts) + (scipy.random.randn(len(ts)) - 0.5) * 3

# The central graphics view

main_chart = window.lineChart

def draw_central_graphics():
    scene = QtWidgets.QGraphicsScene(main_chart)
    main_chart.setScene(scene)

    def text(label, *args):
        scene.addText(label, G_FONT).setPos(*args)

    def line(*args):
        scene.addLine(*args)

    def dot(x, y, *args):
        scene.addEllipse(x-5, y-5, 10, 10, *args)

#   Axes
    text('S', -60, 0)
    text('N', 330, 0)
    text('W Up', 0, -330)
    text('E Down', 0, 330)
    text('Div.= 2.0e-03', 100, 330)

#   Ticks
    line(0, 310, 0, -310)
    for y in scipy.arange(-300, 310, 60): line(-3, y, 3, y)
    line(-20, 0, 310, 0)
    for x in scipy.arange(0, 310, 60): line(x, 3, x, -3)

#   Curves
    p = QtGui.QPainterPath(QtCore.QPoint(120, f(120)))
    for x in range(120, 300): p.lineTo(x, f(x))
    scene.addPath(p)

    p = QtGui.QPainterPath(QtCore.QPoint(120, g(120)))
    for x in range(120, 360, 10): p.lineTo(x, g(x))
    scene.addPath(p, DASH_PEN)

#   Data items
    for t, x, y in zip(ts, xs, ys):
        dot(t, x, BLACK, BLACK_BRUSH)
        dot(t, y, BLACK, WHITE_BRUSH)

radar = window.radarChart

def draw_radar_chart():
    scene = QtWidgets.QGraphicsScene(radar)
    radar.setScene(scene)

#   Rulers
    scene.addLine(-300, 0, -294, 0)
    scene.addLine(+300, 0, +294, 0)
    scene.addLine(0, -300, 0, -294)
    scene.addLine(0, +300, 0, +294)
    scene.addLine(-10, 0, 10, 0)
    scene.addLine(0, -10, 0, 10)
    scene.addEllipse(-300, -300, 600, 600, BLACK)

#   Data items
    for x, y in zip(xs, ys):
        scene.addEllipse(x, y, 10, 10, BLACK, BLACK_BRUSH)

altitude_list()
draw_central_graphics()
draw_radar_chart()

window.show()

app.exec()
