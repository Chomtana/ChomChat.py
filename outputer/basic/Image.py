from ChomChat.Outputer import Component


class Image(Component):
    name: str = 'Image'
    src: str
    ratio: str = '16:9'
    action: Component

    def __init__(self, src: str, action: Component = None, ratio: str = '16:9'):
        self.src = src
        self.ratio = ratio
        self.action = action

    def format_line(self):
        result = {
            "type": "image",
            "url": self.src,
            "size": "full",
            "aspectRatio": self.ratio,
            "aspectMode": "cover"
        }

        if self.action is not None:
            result['action'] = self.action.format_line()

        return result
