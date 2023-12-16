# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MPK225/MPK225.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 2569 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.ControlSurface as ControlSurface
import _Framework.DeviceComponent as DeviceComponent
import _Framework.DrumRackComponent as DrumRackComponent
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
import _Framework.Layer as Layer
from _Framework.MidiMap import MidiMap as MidiMapBase
from _Framework.MidiMap import make_button, make_encoder
import _Framework.TransportComponent as TransportComponent

class MidiMap(MidiMapBase):

    def __init__(self, *a, **k):
        (super(MidiMap, self).__init__)(*a, **k)
        self.add_button('Play', 0, 118, MIDI_CC_TYPE)
        self.add_button('Record', 0, 119, MIDI_CC_TYPE)
        self.add_button('Stop', 0, 117, MIDI_CC_TYPE)
        self.add_button('Loop', 0, 114, MIDI_CC_TYPE)
        self.add_button('Forward', 0, 116, MIDI_CC_TYPE)
        self.add_button('Backward', 0, 115, MIDI_CC_TYPE)
        self.add_matrix('Encoders', make_encoder, 0, [[22,23,24,25,26,27,28,29]], MIDI_CC_TYPE)
        self.add_matrix('Drum_Pads', make_button, 1, [
         [
          67, 69, 71, 72], [60, 62, 64, 65]], MIDI_NOTE_TYPE)


class MPK225(ControlSurface):

    def __init__(self, *a, **k):
        (super(MPK225, self).__init__)(*a, **k)
        with self.component_guard():
            midimap = MidiMap()
            drum_rack = DrumRackComponent(name='Drum_Rack',
              is_enabled=False,
              layer=Layer(pads=(midimap['Drum_Pads'])))
            drum_rack.set_enabled(True)
            transport = TransportComponent(name='Transport',
              is_enabled=False,
              layer=Layer(play_button=(midimap['Play']),
              record_button=(midimap['Record']),
              stop_button=(midimap['Stop']),
              seek_forward_button=(midimap['Forward']),
              seek_backward_button=(midimap['Backward']),
              loop_button=(midimap['Loop'])))
            transport.set_enabled(True)
            device = DeviceComponent(name='Device',
              is_enabled=False,
              layer=Layer(parameter_controls=(midimap['Encoders'])),
              device_selection_follows_track_selection=True)
            device.set_enabled(True)
            self.set_device_component(device)