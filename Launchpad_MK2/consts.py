# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_MK2/consts.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 748 bytes
from __future__ import absolute_import, print_function, unicode_literals
PRODUCT_ID_BYTES = (0, 32, 41, 105, 0, 0, 0)
IDENTITY_REQUEST = (240, 126, 127, 6, 1, 247)
STANDARD_SYSEX_PREFIX = (240, 0, 32, 41, 2, 24)
CHALLENGE_RESPONSE_BYTE = (64, )
LAYOUT_CHANGE_BYTE = (34, )
FADER_SETUP_BYTE = (43, )
QUIT_MESSAGE = (240, 0, 32, 41, 2, 24, 64, 247)
BLINK_LED_CHANNEL = 1
PULSE_LED_CHANNEL = 2
USER_MODE_CHANNELS = (5, 6, 7, 13, 14, 15)
VOLUME_MODE_CHANNEL = 3
PAN_MODE_CHANNEL = 4
SEND_A_MODE_CHANNEL = 8
SEND_B_MODE_CHANNEL = 9
FADER_STANDARD_TYPE = 0
FADER_BIPOLAR_TYPE = 1
SESSION_WIDTH = 8