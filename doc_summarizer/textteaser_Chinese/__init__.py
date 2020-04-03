# !/usr/bin/python
# -*- coding: utf-8 -*-

from .summarizer import Summarizer


class TextTeaserChinese(object):

    def __init__(self, stopWordsPath, text):
        self.summarizer = Summarizer(stopWordsPath, text)

    def summarize(self, title, text, category="Undefined", source="Undefined", count=5):
        result = self.summarizer.summarize(text, title, source, category)
        result = self.summarizer.sortSentences(result[:count])
        result = [res['sentence'] for res in result]

        return result
