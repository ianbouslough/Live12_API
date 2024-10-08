# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/BCR2000/config.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 3811 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {
  'STOP': GENERIC_STOP,
  'PLAY': GENERIC_PLAY,
  'REC': GENERIC_REC,
  'LOOP': GENERIC_LOOP,
  'RWD': GENERIC_RWD,
  'FFWD': GENERIC_FFWD}
DEVICE_CONTROLS = (
 GENERIC_ENC1,
 GENERIC_ENC2,
 GENERIC_ENC3,
 GENERIC_ENC4,
 GENERIC_ENC5,
 GENERIC_ENC6,
 GENERIC_ENC7,
 GENERIC_ENC8)
VOLUME_CONTROLS = (97, 98, 99, 100, 101, 102, 103, 104)
TRACKARM_CONTROLS = (
 GENERIC_BUT1,
 GENERIC_BUT2,
 GENERIC_BUT3,
 GENERIC_BUT4,
 GENERIC_BUT5,
 GENERIC_BUT6,
 GENERIC_BUT7,
 GENERIC_BUT8)
BANK_CONTROLS = {
  'TOGGLELOCK': GENERIC_BUT9,
  'BANKDIAL': -1,
  'NEXTBANK': -1,
  'PREVBANK': -1,
  'BANK1': GENERIC_PAD1,
  'BANK2': GENERIC_PAD2,
  'BANK3': GENERIC_PAD3,
  'BANK4': GENERIC_PAD4,
  'BANK5': GENERIC_PAD5,
  'BANK6': GENERIC_PAD6,
  'BANK7': GENERIC_PAD7,
  'BANK8': GENERIC_PAD8}
CONTROLLER_DESCRIPTION = {'INPUTPORT':'BCR2000', 
 'OUTPUTPORT':'BCR2000',  'CHANNEL':0}
MIXER_OPTIONS = {
  'NUMSENDS': 2,
  'SEND1': GENERIC_SLIDERS,
  'SEND2': (89, 90, 91, 92, 93, 94, 95, 96),
  'MASTERVOLUME': -1}