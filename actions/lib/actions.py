from st2actions.runners.pythonrunner import Action
import soco


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self._sonos = self._get_client()
        self._speakers = None

    def _get_client(self):
        return soco.SoCo

    def _get_speakers(self):
        speakers = soco.discover()
        self._speakers = speakers
        return speakers
