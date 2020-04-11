from ChomChat.Outputer import Component


class LinkAction(Component):
    name: str = 'LinkAction'
    url: str

    def __init__(self, url):
        self.url = url

    def format_line(self):
        return {
            "type": "uri",
            "uri": self.url
        }
