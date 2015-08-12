from lib.actions import BaseAction


class GetCurrentTrackInfoAction(BaseAction):
    def run(self, ip):
        speaker = self._sonos(ip)
        return speaker.get_current_track_info()
