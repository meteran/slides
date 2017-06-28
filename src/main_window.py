#!/usr/bin/env python
# coding: utf-8
import os

from PyQt5.QtCore import QDir
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QFileSystemModel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QTreeView
from PyQt5.uic import loadUi

from src.screen import Screen
from src.texts import Text


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # just for PyCharm autocomplete
        self.directory_view = QTreeView()
        self.edit_view = QPlainTextEdit()

        loadUi('UI/slides.ui', self)

        self.file_model = QFileSystemModel(self)
        self.file_model.setRootPath('')
        self.file_model.setFilter(QDir.Files | QDir.AllDirs | QDir.NoDotAndDotDot)
        self.file_model.setNameFilters(['*.sld'])
        self.directory_view.setModel(self.file_model)
        self.directory_view.hideColumn(1)
        self.directory_view.hideColumn(2)
        self.directory_view.hideColumn(3)

        self.text = None

        self.screen = Screen(parent=self)
        # self.screen.show()

        self.directory_view.doubleClicked.connect(self.open_file)

    def open_file(self, model: QModelIndex):
        path = str(self.file_model.filePath(model))
        if os.path.isfile(path) and path.endswith('.sld'):
            self.text = Text(path)

            self.edit_view.setPlainText(self.text.text)
