from lib.action import BaseAction


class PauseAction(BaseAction):
    def run(self, ip):
        speaker = self._sonos(ip)
        return speaker.pause()
