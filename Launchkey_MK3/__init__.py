# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK3/__init__.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1074 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, SYNC, controller_id, inport, outport
from .launchkey_mk3 import Launchkey_MK3

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661,
                          product_ids=[
                         308,309,310,311,320],
                          model_name=[
                         'Launchkey MK3 25',
                         'Launchkey MK3 37',
                         'Launchkey MK3 49',
                         'Launchkey MK3 61',
                         'Launchkey MK3 88']), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE]),
                 inport(props=[NOTES_CC, SCRIPT]),
                 outport(props=[SYNC, REMOTE]),
                 outport(props=[NOTES_CC, SCRIPT])]}


def create_instance(c_instance):
    return Launchkey_MK3(c_instance=c_instance)