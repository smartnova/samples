import sys
from PyQt5 import QtGui, QtSvg
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv) 
svgWidget = QtSvg.QSvgWidget('Android_sample.svg')
svgWidget.setGeometry(50,50,759,668)
svgWidget.show()

sys.exit(app.exec_())
