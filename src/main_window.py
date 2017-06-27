#!/usr/bin/env python
# coding: utf-8
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QFileSystemModel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from src.screen import Screen


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        loadUi('UI/slides.ui', self)

        self.file_model = QFileSystemModel(self)
        self.file_model.setRootPath('')
        self.directory_view.setModel(self.file_model)
        self.directory_view.hideColumn(1)
        self.directory_view.hideColumn(2)
        self.directory_view.hideColumn(3)

        self.screen = Screen(parent=self)
        self.screen.show()
        self.screen.set_content('yolodddddddddddddddddddddddddddddddddd\r\nsadsad\r\nfsdif')
        self.screen.set_content('yoloddddddddddddddddddddddddddddddd\r\nsadsad\r\nfsdif')
        self.screen.set_content('yolodddddddddddddddddddddddddddddddddddddddd\r\nsadsad\r\nfsdif')
        self.screen.set_content('yolodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\r\nsadsad\r\nfsdif')
        self.screen.showFullScreen()

        self.action_dir = QAction()
        # self.action_dir.changed

