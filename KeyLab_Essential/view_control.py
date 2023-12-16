# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/view_control.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 902 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import BasicSceneScroller, ScrollComponent
from ableton.v2.control_surface.components import ViewControlComponent as ViewControlComponentBase
from ableton.v2.control_surface.control import StepEncoderControl

class ViewControlComponent(ViewControlComponentBase):
    scene_scroll_encoder = StepEncoderControl(num_steps=64)

    def __init__(self, *a, **k):
        (super(ViewControlComponent, self).__init__)(*a, **k)
        self._scroll_scenes = ScrollComponent((BasicSceneScroller()), parent=self)

    @scene_scroll_encoder.value
    def scene_scroll_encoder(self, value, _):
        if value > 0:
            self._scroll_scenes.scroll_down()
        else:
            if value < 0:
                self._scroll_scenes.scroll_up()