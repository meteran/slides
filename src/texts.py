#!/usr/bin/env python
# coding: utf-8
import os
import re

from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton


class Text(QObject):
    text_changed = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        self._parent = parent
        self._current_index = 0

    def __getitem__(self, item):
        return self._pages[item]

    @property
    def current_page(self):
        return self[self._current_index]

    def reset_index(self):
        self._current_index = 0

    @property
    def next(self):
        if self._current_index+1 == len(self._pages):
            raise StopIteration()

        page = self.current_page
        self._current_index += 1
        return page

    @property
    def previous(self):
        if self._current_index == 0:
            raise StopIteration()

        page = self.current_page
        self._current_index -= 1
        return page

    def __iter__(self):
        return self

    def __next__(self):
        return self.next

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        self._pages = re.split('---+', self._text)
        if self._current_index >= len(self._pages):
            self._current_index = len(self._pages) - 1
        print(text)
        self.text_changed.emit()

    def update(self, text):
        self.text = text


# TODO here should be path to file
class PersistenceManager:
    def __init__(self, parent, edit_view, text: Text):
        self._edit_view = edit_view
        self._parent = parent
        self._text = text
        self._path = None

    def new_path(self):
        path, etx = QFileDialog.getSaveFileName(parent=self._parent, filter='*.sld')
        return path

    @property
    def path(self):
        if not self._path:
            self._path = self.new_path()
        return self._path

    def save(self):
        path = self.path
        if path:
            with open(path, 'w') as fp:
                fp.write(self._text.text)
            self._parent.action_save.setDisabled(True)

    def save_as(self):
        path = self.new_path()
        if path:
            self._path = path
            self.save()

    def new(self):
        override = True
        if self._parent.action_save.isEnabled():
            dialog = QMessageBox(self._parent)
            dialog.setText('Czy chcesz usunąć niezapisane zmiany?')
            dialog.setWindowTitle('Alert')
            dialog.addButton(QPushButton('Tak'), QMessageBox.YesRole)
            dialog.addButton(QPushButton('Anuluj'), QMessageBox.NoRole)
            override = dialog.exec_() == 0

        if override:
            self._path = None
            self._parent.edit_view.setPlainText('')
            self._parent.action_save.setDisabled(True)

    def open(self, path):
        if os.path.isfile(path) and path.endswith('.sld'):
            with open(path, 'r') as fp:
                t = fp.read()
                self._edit_view.setPlainText(t)
        self._parent.action_save.setDisabled(True)
        self._path = path
