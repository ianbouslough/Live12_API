# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/SL_MkIII/sysex.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 2051 bytes
from __future__ import absolute_import, print_function, unicode_literals
SYSEX_START_BYTE = 240
SYSEX_END_BYTE = 247
NOVATION_MANUFACTURER_ID = (0, 32, 41)
SL_MKIII_PRODUCT_ID = (2, 10)
DEVICE_FAMILY_CODE = (1, 1)
DEVICE_FAMILY_MEMBER_CODE = (0, 0)
INCONTROL_COMMAND_ID_BYTE = 1
SET_SCREEN_LAYOUT_COMMAND_BYTE = 1
SET_PROPERTY_COMMAND_BYTE = 2
SET_LED_COMMAND_BYTE = 3
SET_NOTIFICATION_COMMAND_BYTE = 4
TEXT_PROPERTY_BYTE = 1
COLOR_PROPERTY_BYTE = 2
VALUE_PROPERTY_BYTE = 3
EMPTY_SCREEN_LAYOUT_BYTE = 0
KNOB_SCREEN_LAYOUT_BYTE = 1
BOX_SCREEN_LAYOUT_BYTE = 2
SOLID_COLOR_LED_BYTE = 1
STD_MSG_HEADER = (
 SYSEX_START_BYTE,) + NOVATION_MANUFACTURER_ID + SL_MKIII_PRODUCT_ID + (INCONTROL_COMMAND_ID_BYTE,)
SHOW_MESSAGE_MSG_HEADER = STD_MSG_HEADER + (SET_NOTIFICATION_COMMAND_BYTE,)
SET_SCREEN_LAYOUT_MESSAGE_HEADER = STD_MSG_HEADER + (SET_SCREEN_LAYOUT_COMMAND_BYTE,)
SET_PROPERTY_MSG_HEADER = STD_MSG_HEADER + (SET_PROPERTY_COMMAND_BYTE,)
SET_LED_MSG_HEADER = STD_MSG_HEADER + (SET_LED_COMMAND_BYTE,)
NUM_SET_PROPERTY_HEADER_BYTES = 3
SYSEX_MSG_MAX_LENGTH = 256
INNER_MESSAGE_MAX_LENGTH = SYSEX_MSG_MAX_LENGTH - len(SET_PROPERTY_MSG_HEADER) - 1

def wrap_message(message):
    return SET_PROPERTY_MSG_HEADER + message + (SYSEX_END_BYTE,)


def collate_message_segments(segments):
    if not segments:
        return []
    collated = []
    offset = 0
    for index, segment in enumerate(segments):
        if len(collated) + len(segment) > INNER_MESSAGE_MAX_LENGTH:
            break
        else:
            collated.extend(segment)
            offset = index

    return [
     tuple(collated)] + collate_message_segments(segments[offset + 1:])


def make_sysex_from_segments(segments):
    return list(map(wrap_message, collate_message_segments(segments)))