from ChomChat.Outputer import Component


class Text(Component):
    name: str = 'Text'
    message: str

    def __init__(self, message: str):
        self.message = message

    def format_line(self):
        return {
            "type": "text",
            "text": self.message,
            "wrap": True
        }