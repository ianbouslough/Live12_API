# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/settings.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 689 bytes
from __future__ import absolute_import, print_function, unicode_literals
from pushbase.setting import OnOffSetting

def create_settings(preferences=None):
    preferences = preferences if preferences is not None else {}
    return {'workflow':OnOffSetting(name='Workflow',
       value_labels=[
      'Scene', 'Clip'],
       default_value=True,
       preferences=preferences), 
     'aftertouch_mode':OnOffSetting(name='Pressure',
       value_labels=[
      'Mono', 'Polyphonic'],
       default_value=True,
       preferences=preferences)}