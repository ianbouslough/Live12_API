# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/layer.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 695 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Layer as LayerBaseClass

class Layer(LayerBaseClass):

    def on_received(self, client, *a, **k):
        (super().on_received)(client, *a, **k)
        client.num_layers += 1

    def on_lost(self, client):
        super().on_lost(client)
        client.num_layers -= 1