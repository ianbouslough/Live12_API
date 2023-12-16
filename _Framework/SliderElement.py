# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/SliderElement.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 619 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from .EncoderElement import EncoderElement
from .InputControlElement import MIDI_NOTE_TYPE

class SliderElement(EncoderElement):

    def __init__(self, msg_type, channel, identifier, *a, **k):
        (super(SliderElement, self).__init__)(
 msg_type, channel, identifier, *a, map_mode=Live.MidiMap.MapMode.absolute, **k)