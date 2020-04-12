from ChomChat import StateBase


class GroupState(StateBase):
    def __init__(self, parent, name, default=None):
        super().__init__(parent, name, default)
        self._self_mode = True

    def _before_set(self, value, old, path):
        if not isinstance(value, dict): raise Exception('Value of GroupState should be dict got '+value)
        for (key, value) in value.items():
            if key in self.__class__.__dict__:
                self.__class__.__dict__[key].__set__(self, value)
        super()._before_set(value, old, path)

    def _after_set(self, value, old, path):
        super()._after_set(value, old, path)
