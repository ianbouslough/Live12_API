# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/AIRA_MX_1/__init__.py
# Compiled at: 2023-12-07 14:24:09
# Size of source mod 2**32: 718 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, PORTS_KEY, SCRIPT, controller_id, inport, outport
from .RolandMX1 import RolandMX1

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=1410,
                          product_ids=[419],
                          model_name=['MX-1']), 
     
     PORTS_KEY: [
                 inport(props=[]),
                 inport(props=[SCRIPT]),
                 outport(props=[]),
                 outport(props=[SCRIPT])]}


def create_instance(c_instance):
    return RolandMX1(c_instance=c_instance)