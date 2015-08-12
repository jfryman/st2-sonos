from lib.actions import BaseAction
from soco import SonosDiscovery


class GetSpeakerIpsAction(BaseAction):
    def run(self):
        sonos = SonosDiscovery()
        return sonos.get_speaker_ips()
