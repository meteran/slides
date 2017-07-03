#!/usr/bin/env python
# coding: utf-8
import os
import re

from PyQt5.QtWidgets import QMainWindow


class Text:
    def __init__(self):
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

    def update(self, text):
        self.text = text


# TODO here should be path to file
class PersistenceManager:
    def __init__(self, parent, edit_view, text: Text):
        self.edit_view = edit_view
        self.parent = parent
        self.text = text
        self._path = None

    def save(self):
        if self._path:
            with open(self._path, 'w') as fp:
                fp.write(self.text.text)

    def save_as(self):
        print('saving as')

    def new(self):
        self._path = None
        self.parent.edit_view.setPlainText('')
        self.parent.action_save.setDisabled(True)

    def open(self, path):
        if os.path.isfile(path) and path.endswith('.sld'):
            with open(path, 'r') as fp:
                self.edit_view.setPlainText(fp.read())
            self.text.path = path
        self.parent.action_save.setDisabled(True)
