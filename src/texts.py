#!/usr/bin/env python
# coding: utf-8
import re


class Text:
    def __init__(self):
        self._path = None
        self._current_index = 0

    def __getitem__(self, item):
        return self._pages[item]

    @property
    def current_page(self):
        return self[self._current_index]

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

    def save(self):
        if self._path:
            with open(self._path, 'w') as fp:
                fp.write(self._text)
