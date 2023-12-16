# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/view/util.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 542 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import List, Optional
from ..state import State

def suppress_notifications(state: State, exclude: Optional[List[str]]=None):
    if exclude is None:
        exclude = []
    for notification in getattr(state, '_notifications', set()) - set(exclude):
        setattr(state, notification, None)