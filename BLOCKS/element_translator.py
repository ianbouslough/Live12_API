# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/BLOCKS/element_translator.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 821 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object

class ElementTranslator(object):

    def __init__(self, elements=None, feedback_channel=None, non_feedback_channel=None, *a, **k):
        (super(ElementTranslator, self).__init__)(*a, **k)
        self._elements = elements
        self._feedback_channel = feedback_channel
        self._non_feedback_channel = non_feedback_channel

    def set_enabled(self, enable):
        for element in self._elements:
            channel = self._non_feedback_channel
            if enable:
                element.reset_state()
                channel = self._feedback_channel
            else:
                element.set_channel(channel)