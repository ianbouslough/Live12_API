# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC40/TransportComponent.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 2055 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.Control import ButtonControl
from _Framework.SubjectSlot import subject_slot
from _Framework.TransportComponent import TransportComponent as TransportComponentBase

class TransportComponent(TransportComponentBase):
    rec_quantization_button = ButtonControl()

    def __init__(self, *a, **k):
        (super(TransportComponent, self).__init__)(*a, **k)
        self._last_quant_value = Live.Song.RecordingQuantization.rec_q_eight
        self._on_quantization_changed.subject = self.song()
        self._update_quantization_state()
        self.set_quant_toggle_button = self.rec_quantization_button.set_control_element

    @rec_quantization_button.pressed
    def rec_quantization_button(self, value):
        quant_value = self.song().midi_recording_quantization
        if quant_value != Live.Song.RecordingQuantization.rec_q_no_q:
            self._last_quant_value = quant_value
            self.song().midi_recording_quantization = Live.Song.RecordingQuantization.rec_q_no_q
        else:
            self.song().midi_recording_quantization = self._last_quant_value

    @subject_slot('midi_recording_quantization')
    def _on_quantization_changed(self):
        if self.is_enabled():
            self._update_quantization_state()

    def _update_quantization_state(self):
        quant_value = self.song().midi_recording_quantization
        quant_on = quant_value != Live.Song.RecordingQuantization.rec_q_no_q
        if quant_on:
            self._last_quant_value = quant_value
        self.rec_quantization_button.color = 'DefaultButton.On' if quant_on else 'DefaultButton.Off'