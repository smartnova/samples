from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize

class ChartView(QtWidgets.QGraphicsView):
    def __init__(self, *args):
        super().__init__(*args)

    def sizeHint(self):
        return QSize(100, 100)

    def resizeEvent(self, ev=None):
        if self.scene() is not None:
            self.fitInView(self.scene().sceneRect(), Qt.KeepAspectRatio)
            print(self.accessibleName(), self.sizeHint())
