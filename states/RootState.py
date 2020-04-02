from ChomChat.ChomChat import StateBase

class RootState(StateBase):
    def __init__(self, context):
        self.context = context
        self.value = None
