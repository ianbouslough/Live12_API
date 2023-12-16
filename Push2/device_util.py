# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/device_util.py
# Compiled at: 2023-11-21 04:17:31
# Size of source mod 2**32: 1134 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import liveobj_valid

def is_drum_pad(item):
    return liveobj_valid(item) and isinstance(item, Live.DrumPad.DrumPad)


def find_chain_or_track(item):
    if is_drum_pad(item) and item.chains:
        chain = item.chains[0]
    else:
        chain = item
        while liveobj_valid(chain):
            if not isinstance(chain, (Live.Track.Track, Live.Chain.Chain)):
                chain = getattr(chain, 'canonical_parent', None)

    return chain


def find_rack(item):
    rack = item
    while liveobj_valid(rack):
        if not isinstance(rack, Live.RackDevice.RackDevice):
            rack = getattr(rack, 'canonical_parent', None)

    return rack