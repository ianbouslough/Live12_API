# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_A/__init__.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 484 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import SUGGESTED_PORT_NAMES_KEY
from .komplete_kontrol_a import Komplete_Kontrol_A

def get_capabilities():
    return {SUGGESTED_PORT_NAMES_KEY: ['Komplete Kontrol A DAW', 'Komplete Kontrol M DAW']}


def create_instance(c_instance):
    return Komplete_Kontrol_A(c_instance=c_instance)