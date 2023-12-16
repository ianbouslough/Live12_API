# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK2/ControlElementUtils.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1372 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
import Live
import _Framework.ButtonElement as ButtonElement
import _Framework.ButtonMatrixElement as ButtonMatrixElement
import _Framework.ComboElement as ComboElement
from _Framework.Dependency import depends
import _Framework.EncoderElement as EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from _Framework.Resource import PrioritizedResource
import _Framework.SliderElement as SliderElement
from .consts import STANDARD_CHANNEL

@depends(skin=None)
def make_button(identifier, msg_type=MIDI_NOTE_TYPE, is_momentary=True, skin=None, is_modifier=False, name=''):
    return ButtonElement(is_momentary,
      msg_type,
      STANDARD_CHANNEL,
      identifier,
      skin=skin,
      name=name,
      resource_type=(PrioritizedResource if is_modifier else None))


def make_encoder(identifier, name=''):
    return EncoderElement(MIDI_CC_TYPE,
      STANDARD_CHANNEL,
      identifier,
      (Live.MidiMap.MapMode.absolute),
      name=name)


def make_slider(identifier, name='', channel=STANDARD_CHANNEL):
    return SliderElement(MIDI_CC_TYPE, channel, identifier, name=name)