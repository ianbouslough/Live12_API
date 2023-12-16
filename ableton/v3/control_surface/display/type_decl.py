# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/type_decl.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1109 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import Any, Callable, NamedTuple, TypeVar
from .state import State

class Event(NamedTuple):
    name: str
    origin: Any
    value: Any


INIT_EVENT = Event(name='init', origin=None, value=None)
DISCONNECT_EVENT = Event(name='disconnect', origin=None, value=None)
ContentType = TypeVar('ContentType')
Render = Callable[([State], ContentType)]