# -*- coding: utf-8 -*-

from section import Section


class Text(Section):
    def __init__(self, text):
        super(Text, self).__init__('text', text)
        self.text = text

    def convert(self, converter):
        return converter.text(self.text)
