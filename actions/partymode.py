from lib.actions import BaseAction


class PartyModeAction(BaseAction):
    def run(self, ip):
        speaker = self._sonos(ip)
        return speaker.partymode()
