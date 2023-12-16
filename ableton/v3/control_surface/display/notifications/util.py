# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/notifications/util.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 597 bytes
from __future__ import absolute_import, annotations, print_function, unicode_literals
from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from typing_extensions import LiteralString
else:
    LiteralString = str

def toggle_text_generator(format_string: 'LiteralString') -> 'Callable[[bool], str]':

    def notification_fn(is_on):
        return format_string.format('on' if is_on else 'off')

    return notification_fn