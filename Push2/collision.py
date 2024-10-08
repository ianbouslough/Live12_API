# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/collision.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 2522 bytes
from __future__ import absolute_import, print_function, unicode_literals
from enum import IntEnum
from ableton.v2.base import EventObject, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator, get_parameter_by_name

class CollisionDeviceDecorator(LiveObjectDecorator, EventObject):

    class ResBodyChooser(IntEnum):
        res1 = 0
        res2 = 1

    class LFOChooser(IntEnum):
        lfo1 = 0
        lfo2 = 1

    class ModSource(IntEnum):
        key = 0
        vel = 1
        env = 2
        lfo1 = 3
        lfo2 = 4
        pb = 5
        mw = 6
        press = 7
        slide = 8

    class ModDest(IntEnum):
        mallet = 0
        noise = 1
        res1 = 2
        res2 = 3
        lfo = 4

    def __init__(self, *a, **k):
        (super(CollisionDeviceDecorator, self).__init__)(*a, **k)
        self._add_enum_parameter(name='Resonator',
          values=[
         'Res 1', 'Res 2'],
          default_value=(self.ResBodyChooser.res1))
        self._add_enum_parameter(name='LFO Select',
          values=[
         'LFO 1', 'LFO 2'],
          default_value=(self.LFOChooser.lfo1))
        self._add_enum_parameter(name='Mod Source',
          values=[
         'Key',
         'Vel',
         'Env',
         'LFO 1',
         'LFO 2',
         'PB',
         'Modwheel',
         'Press',
         'Slide'],
          default_value=(self.ModSource.key))
        self._add_enum_parameter(name='Mod Dest',
          values=[
         'Mallet','Noise','Res 1','Res 2','LFO'],
          default_value=(self.ModDest.mallet))
        self._add_switch_option(name='Structure',
          pname='Structure',
          labels=['1 > 2', '1 + 2'])
        self._add_on_off_option(name='Mallet', pname='Mallet On/Off')
        self._add_on_off_option(name='Noise', pname='Noise On/Off')
        self._add_on_off_option(name='Res 1', pname='Res 1 On/Off')
        self._add_on_off_option(name='Res 2', pname='Res 2 On/Off')
        self._add_on_off_option(name='LFO 1', pname='LFO 1 On/Off')
        self._add_on_off_option(name='LFO 2', pname='LFO 2 On/Off')
        self._add_on_off_option(name='LFO 1 Retrig', pname='LFO 1 Retrigger')
        self._add_on_off_option(name='LFO 2 Retrig', pname='LFO 2 Retrigger')
        self.register_disconnectables(self.options)