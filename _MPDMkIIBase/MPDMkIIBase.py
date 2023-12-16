# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_MPDMkIIBase/MPDMkIIBase.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 2862 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.ButtonElement as ButtonElement
import _Framework.ButtonMatrixElement as ButtonMatrixElement
import _Framework.ControlSurface as ControlSurface
import _Framework.DeviceComponent as DeviceComponent
import _Framework.DrumRackComponent as DrumRackComponent
from _Framework.InputControlElement import MIDI_NOTE_TYPE
import _Framework.Layer as Layer
import _Framework.MixerComponent as MixerComponent
import _Framework.TransportComponent as TransportComponent

class MPDMkIIBase(ControlSurface):

    def __init__(self, pad_ids=None, pad_channel=None, *a, **k):
        (super(MPDMkIIBase, self).__init__)(*a, **k)
        self._pad_ids = pad_ids
        self._pad_channel = pad_channel
        self._pads = None
        self._sliders = None
        self._encoders = None
        self._stop_button = None
        self._play_button = None
        self._record_button = None
        self._control_buttons = None
        with self.component_guard():
            self._create_controls()
            self._create_drums()

    def _create_controls(self):
        self._create_pads()

    def _create_pads(self):
        self._pads = ButtonMatrixElement(rows=[[ButtonElement(True, MIDI_NOTE_TYPE, (self._pad_channel), pad_id, name=('Pad_%d_%d' % (col_index, row_index))) for col_index, pad_id in enumerate(row)] for row_index, row in enumerate(self._pad_ids)])

    def _create_drums(self):
        self._drums = DrumRackComponent(is_enabled=True, name='Drums')
        self._drums.layer = Layer(pads=(self._pads))

    def _create_device(self):
        self._device = DeviceComponent(is_enabled=True,
          name='Device',
          device_selection_follows_track_selection=True)
        self._device.layer = Layer(parameter_controls=(self._encoders))
        self.set_device_component(self._device)

    def _create_transport(self):
        self._transport = TransportComponent(is_enabled=True, name='Transport')
        self._transport.layer = Layer(play_button=(self._play_button),
          stop_button=(self._stop_button),
          record_button=(self._record_button))

    def _create_mixer(self):
        self._mixer = MixerComponent(is_enabled=True,
          num_tracks=(len(self._sliders)),
          invert_mute_feedback=True,
          name='Mixer')
        self._mixer.layer = Layer(volume_controls=(self._sliders))