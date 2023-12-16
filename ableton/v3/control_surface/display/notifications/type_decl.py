# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/notifications/type_decl.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1155 bytes
from __future__ import absolute_import, annotations, print_function, unicode_literals
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable, Optional, TypeVar, Union
if TYPE_CHECKING:
    from typing_extensions import ParamSpec, TypeVarTuple
    NotificationParams = TypeVarTuple('NotificationParams')
    NotificationParamSpec = ParamSpec('NotificationParamSpec')
else:
    NotificationParams = TypeVar('NotificationParams')
    NotificationParamSpec = ...

@dataclass
class _TransformDefaultText:
    transform_fn = lambda s: s
    transform_fn: 'Callable[[str], str]'


class _DefaultText:
    pass


NotificationFnType = TypeVar('NotificationFnType', bound=Callable)
Notification = Optional[Union[(str, _DefaultText, _TransformDefaultText, NotificationFnType)]]
Fn = Callable[(NotificationParamSpec, Any)]
NOTIFICATION_EVENT_ID = 'notification'