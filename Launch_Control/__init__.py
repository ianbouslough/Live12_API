# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control/__init__.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 665 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, SCRIPT, controller_id, inport, outport
from .LaunchControl import LaunchControl

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661,
                          product_ids=[52],
                          model_name='Launch Control'), 
     
     PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT]), outport(props=[NOTES_CC, SCRIPT])]}


def create_instance(c_instance):
    return LaunchControl(c_instance)