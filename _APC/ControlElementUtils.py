# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_APC/ControlElementUtils.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1509 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
MapMode = Live.MidiMap.MapMode
import _Framework.ButtonElement as ButtonElement
import _Framework.EncoderElement as EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
import _Framework.SliderElement as SliderElement
import _APC.RingedEncoderElement as RingedEncoderElement

def make_button(channel, identifier, *a, **k):
    return ButtonElement(True, MIDI_NOTE_TYPE, channel, identifier, *a, **k)


def make_pedal_button(identifier, *a, **k):
    return ButtonElement(True, MIDI_CC_TYPE, 0, identifier, *a, **k)


def make_slider(channel, identifier, *a, **k):
    return SliderElement(MIDI_CC_TYPE, channel, identifier, *a, **k)


def make_knob(channel, identifier, *a, **k):
    return SliderElement(MIDI_CC_TYPE, channel, identifier, *a, **k)


def make_ring_encoder(encoder_identifer, button_identifier, name='', *a, **k):
    button_name = '%s_Ring_Mode_Button' % name
    button = ButtonElement(False, MIDI_CC_TYPE, 0, button_identifier, name=button_name)
    encoder = RingedEncoderElement(
 MIDI_CC_TYPE, 0, encoder_identifer, (MapMode.absolute), *a, name=name, **k)
    encoder.set_ring_mode_button(button)
    return encoder


def make_encoder(channel, identifier, *a, **k):
    return EncoderElement(
 MIDI_CC_TYPE, channel, identifier, MapMode.relative_two_compliment, *a, **k)