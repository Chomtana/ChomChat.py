from ChomChat.ChomChat import StateBase


class State(StateBase):
    def __init__(self, parent, name, default=None):
        super().__init__(parent, name, default)