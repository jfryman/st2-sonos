from lib.actions import BaseAction


class StopAction(BaseAction):
    def run(self, ip):
        speaker = self._sonos(ip)
        return speaker.stop()
