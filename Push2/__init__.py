# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/__init__.py
# Compiled at: 2023-11-21 04:17:31
# Size of source mod 2**32: 1246 bytes
from __future__ import absolute_import, print_function, unicode_literals

def get_capabilities():
    from ableton.v2.control_surface import capabilities as caps
    return {caps.CONTROLLER_ID_KEY: caps.controller_id(vendor_id=10626,
                               product_ids=[6503],
                               model_name='Ableton Push 2'), 
     
     caps.PORTS_KEY: [
                      caps.inport(props=[caps.HIDDEN, caps.NOTES_CC, caps.SCRIPT]),
                      caps.inport(props=[]),
                      caps.outport(props=[caps.HIDDEN, caps.NOTES_CC, caps.SYNC, caps.SCRIPT]),
                      caps.outport(props=[])], 
     
     caps.TYPE_KEY: 'push2', 
     caps.AUTO_LOAD_KEY: True}


def create_instance(c_instance):
    from .push2 import Push2
    from .push2_model import Root, Sender
    root = Root(sender=Sender(message_sink=(c_instance.send_model_update),
      process_connected=(c_instance.process_connected)))
    return Push2(c_instance=c_instance,
      model=root,
      decoupled_parameter_list_change_notifications=True)