# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Axiom_AIR_25_49_61/IdentifyingEncoderElement.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 3839 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.EncoderElement as EncoderElement
from _Framework.InputControlElement import *

class IdentifyingEncoderElement(EncoderElement):

    def __init__(self, msg_type, channel, identifier, map_mode, send_channel=None, identifier_send_offset=0):
        EncoderElement.__init__(self, msg_type, channel, identifier, map_mode)
        self._identify_mode = False
        self._send_channel = send_channel
        self._identifier_send_offset = identifier_send_offset
        self._on_value = 127
        self._off_value = 0
        self._force_next_value = False

    def set_identify_mode(self, identify_mode):
        if self._identify_mode != identify_mode:
            self._identify_mode = identify_mode
            self._request_rebuild()

    def get_identify_mode(self):
        return self._identify_mode

    def install_connections(self, translate_message, install_mapping, install_forwarding):
        current_parameter = self._parameter_to_map_to
        if self._identify_mode:
            self._parameter_to_map_to = None
        InputControlElement.install_connections(self, translate_message, install_mapping, install_forwarding)
        self._parameter_to_map_to = current_parameter
        self._update_led()

    def set_on_off_values(self, on_value, off_value):
        self.clear_send_cache()
        self._on_value = on_value
        self._off_value = off_value

    def set_force_next_value(self):
        self._force_next_value = True

    def turn_on(self):
        self.send_value(self._on_value)

    def turn_off(self):
        self.send_value(self._off_value)

    def reset(self):
        self.send_value(self._off_value)

    def send_value(self, value, force=False):
        if force or (self._force_next_value or value) != self._last_sent_value and self._is_being_forwarded:
            data_byte1 = self._original_identifier + self._identifier_send_offset
            data_byte2 = value
            status_byte = self._send_channel if self._send_channel else self._original_channel
            if self._msg_type == MIDI_NOTE_TYPE:
                status_byte += MIDI_NOTE_ON_STATUS
            else:
                if self._msg_type == MIDI_CC_TYPE:
                    status_byte += MIDI_CC_STATUS
            if self.send_midi((status_byte, data_byte1, data_byte2)):
                self._last_sent_message = (
                 value, None)
                if self._report_output:
                    is_input = True
                    self._report_value(value, not is_input)
        self._force_next_value = False

    def connect_to(self, parameter):
        if parameter != self._parameter_to_map_to:
            if not self.is_mapped_manually():
                self.send_value((self._off_value), force=True)
        EncoderElement.connect_to(self, parameter)

    def release_parameter(self):
        EncoderElement.release_parameter(self)
        self._update_led()

    def is_mapped_manually(self):
        return not self._is_mapped and not self._is_being_forwarded

    def _update_led(self):
        if self.is_mapped_manually():
            self.send_value((self._on_value), force=True)
        else:
            if self._parameter_to_map_to != None:
                self.send_value((self._on_value), force=True)
            else:
                self.send_value((self._off_value), force=True)