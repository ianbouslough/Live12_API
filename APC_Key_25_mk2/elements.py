# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC_Key_25_mk2/elements.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1342 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import MIDI_NOTE_TYPE, ElementsBase, MapMode, create_matrix_identifiers
from .colors import FULL_BRIGHTNESS_CHANNEL

class Elements(ElementsBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.add_modifier_button(98, 'Shift_Button', msg_type=MIDI_NOTE_TYPE)
        self.add_button(81, 'Stop_All_Clips_Button', msg_type=MIDI_NOTE_TYPE)
        self.add_button(91, 'Play_Button', msg_type=MIDI_NOTE_TYPE)
        self.add_button(93, 'Record_Button', msg_type=MIDI_NOTE_TYPE)
        self.add_button_matrix(create_matrix_identifiers(0, 40, width=8, flip_rows=True),
          'Clip_Launch_Buttons',
          msg_type=MIDI_NOTE_TYPE,
          led_channel=FULL_BRIGHTNESS_CHANNEL)
        self.add_button_matrix([range(64, 72)], 'Track_Buttons', msg_type=MIDI_NOTE_TYPE)
        self.add_button_matrix([
         range(82, 87)],
          'Scene_Launch_Buttons', msg_type=MIDI_NOTE_TYPE)
        self.add_encoder_matrix([
         range(48, 56)],
          'Encoders',
          map_mode=(MapMode.AccelTwoCompliment),
          sensitivity_modifier=(self.shift_button))