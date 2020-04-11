from ChomChat.Outputer import Component


class LineFlexMessage(Component):
    name: str = 'LineFlexMessage'
    message: object

    def __init__(self, message):
        self.message = message

    def format_line(self):
        return self.message
