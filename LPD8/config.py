# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/LPD8/config.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 4566 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {
  'STOP': -1,
  'PLAY': -1,
  'REC': -1,
  'LOOP': -1,
  'RWD': -1,
  'FFWD': -1}
DEVICE_CONTROLS = (
 GENERIC_ENC1,
 GENERIC_ENC2,
 GENERIC_ENC3,
 GENERIC_ENC4,
 GENERIC_ENC5,
 GENERIC_ENC6,
 GENERIC_ENC7,
 GENERIC_ENC8)
VOLUME_CONTROLS = ((-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                   (-1, -1))
TRACKARM_CONTROLS = (-1, -1, -1, -1, -1, -1, -1, -1)
BANK_CONTROLS = {
  'TOGGLELOCK': -1,
  'BANKDIAL': -1,
  'NEXTBANK': -1,
  'PREVBANK': -1,
  'BANK1': -1,
  'BANK2': -1,
  'BANK3': -1,
  'BANK4': -1,
  'BANK5': -1,
  'BANK6': -1,
  'BANK7': -1,
  'BANK8': -1}
PAD_TRANSLATION = ((0, 2, 40, 0), (1, 2, 41, 0), (2, 2, 42, 0), (3, 2, 43, 0), (0, 3, 36, 0),
                   (1, 3, 37, 0), (2, 3, 38, 0), (3, 3, 39, 0))
CONTROLLER_DESCRIPTION = {
  'INPUTPORT': 'LPD8',
  'OUTPUTPORT': 'LPD8',
  'CHANNEL': 0,
  'PAD_TRANSLATION': PAD_TRANSLATION}
MIXER_OPTIONS = {
  'NUMSENDS': 2,
  'SEND1': (-1, -1, -1, -1, -1, -1, -1, -1),
  'SEND2': (-1, -1, -1, -1, -1, -1, -1, -1),
  'MASTERVOLUME': -1}