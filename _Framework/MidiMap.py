# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/MidiMap.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1888 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from .ButtonElement import ButtonElement
from .ButtonMatrixElement import ButtonMatrixElement
from .EncoderElement import EncoderElement
from .SliderElement import SliderElement

def make_button(name, channel, number, midi_message_type):
    is_momentary = True
    return ButtonElement((not is_momentary), midi_message_type, channel, number, name=name)


def make_slider(name, channel, number, midi_message_type):
    return SliderElement(midi_message_type, channel, number, name=name)


def make_encoder(name, channel, number, midi_message_type):
    return EncoderElement(midi_message_type,
      channel, number, (Live.MidiMap.MapMode.absolute), name=name)


class MidiMap(dict):

    def add_button(self, name, channel, number, midi_message_type):
        self[name] = make_button(name, channel, number, midi_message_type)

    def add_matrix(self, name, element_factory, channel, numbers, midi_message_type):

        def one_dimensional_name(base_name, x, _y):
            return '%s[%d]' % (base_name, x)

        def two_dimensional_name(base_name, x, y):
            return '%s[%d,%d]' % (base_name, x, y)

        name_factory = two_dimensional_name if len(numbers) > 1 else one_dimensional_name
        elements = [[element_factory(name_factory(name, column, row), channel, identifier, midi_message_type) for column, identifier in enumerate(identifiers)] for row, identifiers in enumerate(numbers)]
        self[name] = ButtonMatrixElement(rows=elements)