from lib.action import BaseAction


class NextAction(BaseAction):
    def run(self, ip):
        speaker = self._sonos(ip)
        return speaker.next()
