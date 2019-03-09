#!/usr/bin/env python3

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

ui_file = sys.argv[0].replace('.py', '.ui')
window = uic.loadUi(ui_file, QWidget())
window.show()

sys.exit(app.exec_())
