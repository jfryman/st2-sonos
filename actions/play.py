from lib.action import BaseAction


class PlayAction(BaseAction):
    def run(self, ip):
        speaker = self._sonos(ip)
        return speaker.play()
