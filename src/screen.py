#!/usr/bin/env python
# coding: utf-8
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class Screen(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.view = QLabel()
        loadUi('UI/screen.ui', self)

    def set_content(self, content):
        self.view.setText(content)
