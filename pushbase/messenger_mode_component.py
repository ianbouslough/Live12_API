# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/messenger_mode_component.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 2007 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import BooleanContext
from ableton.v2.control_surface.mode import ModesComponent
from .message_box_component import Messenger

class MessengerModesComponent(ModesComponent, Messenger):
    notify_when_enabled = False

    def __init__(self, muted=False, *a, **k):
        (super(MessengerModesComponent, self).__init__)(*a, **k)
        self._mode_message_map = {}
        self._default_and_alternative_mode_map = {}
        self._is_being_enabled = BooleanContext()
        self._muted = muted

    def add_mode(self, name, mode_or_component, message=None, default_mode=None, alternative_mode=None, **k):
        (super(MessengerModesComponent, self).add_mode)(name, mode_or_component, **k)
        self._mode_message_map[name] = message
        self._default_and_alternative_mode_map[name] = (default_mode, alternative_mode)

    def get_mode_message(self):
        message = self._mode_message_map.get(self.selected_mode, '')
        return message

    def get_default_mode_and_alternative_mode(self):
        default_mode, alternative_mode = self._default_and_alternative_mode_map.get(self.selected_mode, '')
        return (
         default_mode, alternative_mode)

    def on_enabled_changed(self):
        with self._is_being_enabled():
            super(MessengerModesComponent, self).on_enabled_changed()

    def _do_enter_mode(self, name):
        super(MessengerModesComponent, self)._do_enter_mode(name)
        if not self._is_being_enabled or self.notify_when_enabled:
            if not self._muted:
                message = self._mode_message_map.get(name, None)
                if message:
                    self.show_notification(message)

    @property
    def muted(self):
        return self._muted

    @muted.setter
    def muted(self, muted):
        self._muted = muted