# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/components/target_track.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 3202 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import filter
from ableton.v2.base import listens, listens_group, liveobj_valid
from ableton.v2.control_surface import Component

class TargetTrackComponent(Component):
    __events__ = ('target_track', )

    def __init__(self, *a, **k):
        (super(TargetTrackComponent, self).__init__)(*a, **k)
        self._target_track = None
        self._armed_track_list = []
        self._TargetTrackComponent__on_selected_track_changed.subject = self.song.view
        self._TargetTrackComponent__on_selected_track_changed()

    @property
    def target_track(self):
        return self._target_track

    @listens('selected_track')
    def __on_selected_track_changed(self):
        if not self._armed_track_list:
            self._set_target_track()

    def _set_target_track(self):
        new_target = self._target_track
        if self._armed_track_list:
            new_target = self._armed_track_list[-1]
        else:
            new_target = self.song.view.selected_track
        if self._target_track != new_target:
            self._target_track = new_target
            self.notify_target_track()


class ArmedTargetTrackComponent(TargetTrackComponent):

    def __init__(self, *a, **k):
        (super(ArmedTargetTrackComponent, self).__init__)(*a, **k)
        self._ArmedTargetTrackComponent__on_tracks_changed.subject = self.song
        self._ArmedTargetTrackComponent__on_tracks_changed()

    @property
    def tracks(self):
        return list(filter(lambda t: liveobj_valid(t) and t.can_be_armed and t.has_midi_input
, self.song.tracks))

    @listens('visible_tracks')
    def __on_tracks_changed(self):
        tracks = self.tracks
        self._ArmedTargetTrackComponent__on_arm_changed.replace_subjects(tracks)
        self._ArmedTargetTrackComponent__on_frozen_state_changed.replace_subjects(tracks)
        self._refresh_armed_track_list()

    @listens_group('arm')
    def __on_arm_changed(self, _):
        self._refresh_armed_track_list()

    @listens_group('is_frozen')
    def __on_frozen_state_changed(self, _):
        self._refresh_armed_track_list()

    def _refresh_armed_track_list(self):
        tracks = self.tracks
        for track in self._armed_track_list:
            if liveobj_valid(track):
                if track.arm:
                    if not track.is_frozen:
                        if track not in tracks:
                            pass
                    self._armed_track_list.remove(track)

        for track in tracks:
            if track.arm:
                if not track.is_frozen:
                    if track not in self._armed_track_list:
                        self._armed_track_list.append(track)

        self._set_target_track()