from lib.action import BaseAction


class InfoAction(BaseAction):
    def run(self, ip):
        speaker = self._sonos(ip)
        return speaker.get_speaker_info()
