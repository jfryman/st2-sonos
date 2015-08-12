from lib.action import BaseAction


class PreviousAction(BaseAction):
    def run(self, ip):
        speaker = self._sonos(ip)
        return speaker.previous()
