from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont, QPen
from PyQt5.QtWidgets import QApplication, QWidget

class Drawing02(QWidget):
    def __init__(self, *args):
        super().__init__()

        self.color = [0, 0, 0]

        self.qp = QPainter()
        self.pen = QPen(QColor(*self.color), 2)
        self.brush = QBrush(QColor(*self.color))
        self.font = QFont('Decorative', 50)

    id_of_slider = { 'redSlider': 0, 'greenSlider': 1, 'blueSlider': 2 }

    def setColor(self):
        slider = self.sender()
        self.color[self.id_of_slider[slider.objectName()]] = slider.value()
        self.pen = QPen(QColor(*self.color), 2)
        self.brush = QBrush(QColor(*self.color))
        self.update()

    def paintEvent(self, event):
        win = self.window()

        super().paintEvent(event)
        s = self.size()
        dx, dy = (s.width() - 640) / 2, (s.height() - 100) / 2

        qp = self.qp
        qp.begin(self)
        qp.setPen(self.pen)
        qp.setBrush(self.brush)
        qp.setRenderHint(QPainter.Antialiasing)

        qp.drawRect(dx + 10, dy + 15, 80, 60)

        qp.drawEllipse(dx + 110, dy + 15, 80, 60)

        qp.drawLine(dx + 210, dy + 15, dx + 270, dy + 75)

        菱形の中心 = QPoint(dx + 290 + 40, dy + 15 + 30)
        菱形の４頂点 = [QPoint(*座標) for 座標 in [[-40, 0], [0, -30], [40, 0], [0, 30]]]
        qp.drawPolygon(*[p + 菱形の中心 for p in 菱形の４頂点])

        qp.setFont(self.font)
        qp.drawText(dx + 390, dy + 75, "I love these figures.")

        qp.end()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    view = Drawing02()
    view.show()
    app.exec()
