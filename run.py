#!/usr/bin/env python3
# coding: utf-8
import sys

import UI.resources
from PyQt5.QtWidgets import QApplication

from src.main_window import MainWindow

if __name__ == '__main__':
    UI.resources.qInitResources()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
