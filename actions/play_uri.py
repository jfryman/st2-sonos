from lib.actions import BaseAction


class PlayURIAction(BaseAction):
    def run(self, ip, uri):
        speaker = self._sonos(ip)
        return speaker.play_uri(uri)
