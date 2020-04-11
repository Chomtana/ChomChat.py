from ChomChat.Outputer import Component


class Button(Component):
    name: str = 'Button'
    label: str
    action: Component

    def __init__(self, label, action: Component = None):
        self.label = label
        self.action = action

    def format_line(self):
        result = {
            "type": "button",
            "style": "link",
            "height": "sm",
        }

        if self.action is not None:
            action = self.action.format_line()
            action['label'] = self.label
            result['action'] = action

        return result
