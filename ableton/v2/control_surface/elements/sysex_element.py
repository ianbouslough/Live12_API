# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/elements/sysex_element.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 3025 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import old_hasattr
from base.dependency import depends
from .. import midi
from ..input_control_element import MIDI_SYSEX_TYPE, InputControlElement

class SysexElement(InputControlElement):

    def __init__(self, send_message_generator=None, enquire_message=None, default_value=None, optimized=False, *a, **k):
        (super(SysexElement, self).__init__)(a, msg_type=MIDI_SYSEX_TYPE, **k)
        self._send_message_generator = send_message_generator
        self._enquire_message = enquire_message
        self._default_value = default_value
        self._optimized = optimized

    def message_map_mode(self):
        raise AssertionError("SysexElement doesn't support mapping.")

    def send_value(self, *arguments):
        message = (self._send_message_generator)(*arguments)
        self._do_send_value(message)

    def enquire_value(self):
        self.send_midi(self._enquire_message)

    def reset(self):
        if self._default_value is not None:
            self.send_value(self._default_value)

    def _do_send_value(self, message):
        if self._optimized:
            if not message != self._last_sent_message or self.send_midi(message):
                self._last_sent_message = message
        else:
            self.send_midi(message)

    @property
    def _last_sent_value(self):
        if self._last_sent_message:
            return self._last_sent_message
        return -1


class ColorSysexElement(SysexElement):

    @depends(skin=None)
    def __init__(self, skin=None, *a, **k):
        (super(ColorSysexElement, self).__init__)(*a, **k)
        self._skin = skin

    def set_light(self, value):
        color = None
        if old_hasattr(value, 'draw'):
            color = value
        else:
            color = self._skin[value]
        color.draw(self)