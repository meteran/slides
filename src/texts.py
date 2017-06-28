#!/usr/bin/env python
# coding: utf-8
import re


class Text:
    def __init__(self, file_path):
        self._path = file_path

        with open(self._path, 'r') as fp:
            self._text = fp.read()

        self._pages = re.split('---+', self._text)

    def __getitem__(self, item):
        return self._pages[item]

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self.update(text)

    def update(self, text):
        self._text = text
        with open(self._path, 'w') as fp:
            fp.write(text)
