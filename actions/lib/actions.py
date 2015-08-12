from st2actions.runners.pythonrunner import Action
import soco


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self._sonos = self._get_client()

    def _get_client(self):
        return soco.SoCo
