# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/SliderElement.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 2413 bytes
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import round
from past.utils import old_div
from _Framework.Skin import Skin, SkinColorMissingError
from _Framework.SliderElement import SliderElement as SliderElementBase
from . import consts
FADER_TYPES = (
 consts.FADER_TYPE_STANDARD, consts.FADER_TYPE_BIPOLAR)

class SliderElement(SliderElementBase):

    def __init__(self, msg_type, channel, identifier, skin=Skin(), *a, **k):
        self._skin = skin
        self._header = None
        self._type = consts.FADER_TYPE_STANDARD
        self._color = 0
        (super(SliderElement, self).__init__)(msg_type, channel, identifier, *a, **k)
        self.set_needs_takeover(False)

    def set_index(self, index):
        self._header = consts.SYSEX_STANDARD_PREFIX + consts.SYSEX_PARAM_BYTE_FADER_SETUP + (index,)

    def set_light_and_type(self, light_value, type_value):
        self.set_light(light_value)
        self._type = type_value

    def set_light(self, value):
        self._set_skin_light(value)

    def _set_skin_light(self, value):
        color = self._skin[value]
        self._color = int(color)

    def install_connections(self, install_translation_callback, install_mapping_callback, install_forwarding_callback):
        super(SliderElement, self).install_connections(install_translation_callback, install_mapping_callback, install_forwarding_callback)
        if len(self.resource.owners) > 0:
            self._setup_fader()

    def _setup_fader(self):
        if self._header:
            param = self._parameter_to_map_to
            if param != None and param.is_enabled:
                p_range = param.max - param.min
                value = int(round(old_div(param.value - param.min, p_range) * 127))
                color_value = self._color
            else:
                value = 0
                color_value = 0
            msg = self._header + (self._type, color_value, value) + consts.SYSEX_STANDARD_SUFFIX
            self._send_midi(msg)

    def update(self):
        if len(self.resource.owners) > 0:
            self._setup_fader()