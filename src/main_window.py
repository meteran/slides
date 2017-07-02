#!/usr/bin/env python
# coding: utf-8
import os

from PyQt5.QtCore import QDir
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtWidgets import QFileSystemModel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenu
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
        self.playlist_dock = QDockWidget()
        self.dir_dock = QDockWidget()
        self.preview_dock = QDockWidget()
        self.action_preview = QAction()
        self.action_dir = QAction()
        self.action_playlist = QAction()
        self.menu_window = QMenu()

        loadUi('UI/slides.ui', self)

        root_path = QDir.currentPath()

        self.file_model = QFileSystemModel(self)
        self.file_model.setFilter(QDir.Files | QDir.AllDirs | QDir.NoDotAndDotDot)
        self.file_model.setNameFilters(['*.sld'])
        self.file_model.setNameFilterDisables(False)
        self.file_model.setRootPath(root_path)

        self.directory_view.setModel(self.file_model)
        self.directory_view.setRootIndex(self.file_model.index(root_path))
        self.directory_view.hideColumn(1)
        self.directory_view.hideColumn(2)
        self.directory_view.hideColumn(3)

        self.menu_window.addAction(self.dir_dock.toggleViewAction())
        self.menu_window.addAction(self.preview_dock.toggleViewAction())
        self.menu_window.addAction(self.playlist_dock.toggleViewAction())

        self.screen = Screen(parent=self)

        self.text = Text()
        self.edit_view.textChanged.connect(lambda: self.text.update(self.edit_view.toPlainText()))

        # TESTS


        # self.screen.show()
        # self.screen.set_content('tekst piosenki')

        self.directory_view.doubleClicked.connect(self.open_file)

    def open_file(self, model: QModelIndex):
        path = str(self.file_model.filePath(model))
        if os.path.isfile(path) and path.endswith('.sld'):
            with open(path, 'r') as fp:
                self.edit_view.setPlainText(fp.read())
            self.text.path = path

