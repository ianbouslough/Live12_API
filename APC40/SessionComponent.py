# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC40/SessionComponent.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1092 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Control import ButtonControl
from _APC.SessionComponent import SessionComponent as SessionComponentBase

class SessionComponent(SessionComponentBase):
    slot_launch_button = ButtonControl()
    selected_scene_launch_button = ButtonControl()

    def set_slot_launch_button(self, button):
        self.slot_launch_button.set_control_element(button)

    @slot_launch_button.pressed
    def slot_launch_button(self, button):
        clip_slot = self.song().view.highlighted_clip_slot
        if clip_slot:
            clip_slot.fire()

    def set_selected_scene_launch_button(self, button):
        self.selected_scene_launch_button.set_control_element(button)

    @selected_scene_launch_button.pressed
    def selected_scene_launch_button(self, button):
        scene = self.song().view.selected_scene
        if scene:
            scene.fire()