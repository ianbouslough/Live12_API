# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_S_Mk3/view_control.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1904 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.components import ViewControlComponent as ViewControlComponentBase
from ableton.v3.control_surface.controls import SendValueEncoderControl

def add_scroll_encoder(component):
    encoder = SendValueEncoderControl()

    @encoder.value
    def encoder(component, value, _):
        if value < 0:
            if component.can_scroll_up():
                component.scroll_up()
        else:
            if component.can_scroll_down():
                component.scroll_down()

    component.add_control('encoder', encoder)


def update_scroll_encoder(component):
    component.encoder.value = int(component.can_scroll_up()) ^ int(component.can_scroll_down() << 1)


class ViewControlComponent(ViewControlComponentBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        add_scroll_encoder(self._scroll_scenes)
        add_scroll_encoder(self._scroll_tracks)

    def set_scene_encoder(self, control):
        self._scroll_scenes.encoder.set_control_element(control)
        self._update_scene_scrollers()

    def set_track_encoder(self, control):
        self._scroll_tracks.encoder.set_control_element(control)
        self._update_track_scrollers()

    def _update_track_scrollers(self):
        super()._update_track_scrollers()
        update_scroll_encoder(self._scroll_tracks)

    def _update_scene_scrollers(self):
        super()._update_scene_scrollers()
        update_scroll_encoder(self._scroll_scenes)