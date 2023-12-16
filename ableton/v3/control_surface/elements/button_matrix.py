# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/elements/button_matrix.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1431 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import slicer, to_slice
from ableton.v2.control_surface.elements import ButtonMatrixElement as ButtonMatrixElementBase
from ...base import lazy_attribute, recursive_map
from ..display import Renderable

class ButtonMatrixElement(ButtonMatrixElementBase, Renderable):

    @property
    @slicer(2)
    def submatrix(self, col_slice, row_slice):
        col_slice = to_slice(col_slice)
        row_slice = to_slice(row_slice)
        rows = [row[col_slice] for row in self._orig_buttons[row_slice]]
        return ButtonMatrixElement(rows=rows)

    @lazy_attribute
    def renderable_state(self):
        if not any((isinstance(button, Renderable) for row in self._orig_buttons for button in row)):
            return
        matrix = recursive_map(lambda button: button.renderable_state if isinstance(button, Renderable) else None
, self._orig_buttons)
        if len(matrix) == 1:
            return matrix[0]
        return matrix