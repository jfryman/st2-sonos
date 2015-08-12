from lib.actions import BaseAction


class GetSpeakerIpsAction(BaseAction):
    def run(self):
        devices = []
        speakers = self._get_speakers()
        for speaker in speakers:
            devices.append(speaker.ip_address)
        return devices
