from ChomChat.State.State import State


class FloatState(State):
    def __init__(self, parent, name, default=None):
        super().__init__(parent, name, default)

    def _after_set(self, value, old, path):
        self._model.value = float(value)
        super()._after_set(value, old, path)