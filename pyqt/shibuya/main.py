import sys

import scipy

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


S = 100
BLACK = QtGui.QColor('black')
WHITE = QtGui.QColor('white')
G_FONT = QtGui.QFont('Times New Roman', 16, 75)
PEN = QtGui.QPen(BLACK)
BLACK_BRUSH = QtGui.QBrush(BLACK, Qt.SolidPattern)
WHITE_BRUSH = QtGui.QBrush(WHITE, Qt.SolidPattern)
DASH_PEN = QtGui.QPen(BLACK_BRUSH, 1, Qt.DashLine)
DOT_PEN = QtGui.QPen(BLACK_BRUSH, 1, Qt.DotLine)

def f(x):
    return (x - 120) * (x - 120) / 120

def g(x):
    return (x - 160) * (x - 160) / 120 - 300

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

# The central graphics view

main_chart = window.lineChart
main_chart.setSceneRect(-S, -S, S * 2, S * 2)

main_scene = QtWidgets.QGraphicsScene()
main_chart.setScene(main_scene)
main_chart.setSceneRect(main_scene.sceneRect())

def draw_central_graphics():
    def text(label, *args):
        main_scene.addText(label, G_FONT).setPos(*args)

    def line(*args):
        main_scene.addLine(*args)

    def dot(x, y, *args):
        main_scene.addEllipse(x-5, y-5, 10, 10, *args)

    text('S', -60, 0)
    text('N', 330, 0)
    text('W Up', 0, -330)
    text('E Down', 0, 330)
    text('Div.= 2.0e-03', 100, 330)
    line(0, 310, 0, -310)
    for y in scipy.arange(-300, 310, 60): line(-10, y, 10, y)
    line(-20, 0, 310, 0)
    for x in scipy.arange(0, 310, 60): line(x, 10, x, -10)

    p = QtGui.QPainterPath(QtCore.QPoint(120, f(120)))
    for x in range(120, 300): p.lineTo(x, f(x))
    main_scene.addPath(p)

    p = QtGui.QPainterPath(QtCore.QPoint(120, g(120)))
    for x in range(120, 360, 10): p.lineTo(x, g(x))
    pen = QtGui.QPen()
    main_scene.addPath(p, DASH_PEN)

    xs = scipy.random.randint(120, 300, 10)
    for x in xs:
        dot(x, f(x) + (scipy.random.randn() - 0.5) * 3, BLACK, BLACK_BRUSH)
        dot(x, g(x) + (scipy.random.randn() - 0.5) * 3, BLACK, WHITE_BRUSH)

def draw_radar_chart():
    pass

altitude_list()
draw_central_graphics()
window.showFullScreen()

main_chart.fitInView(main_scene.sceneRect(), Qt.KeepAspectRatio)

app.exec()
