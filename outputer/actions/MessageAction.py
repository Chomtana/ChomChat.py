from ChomChat.Outputer import Component


class MessageAction(Component):
    name: str = 'MessageAction'
    message: str

    def __init__(self, message):
        self.message = message

    def format_line(self):
        return {
            "type": "message",
            "text": self.message
        }
