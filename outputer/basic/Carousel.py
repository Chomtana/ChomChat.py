from typing import List
from ChomChat.Outputer import Component


class Carousel(Component):
    name: str = 'Carousel'
    children: List[Component]

    def __init__(self, children: List[Component]):
        self.children = children

    def format_line(self):
        return {
            "type": "carousel",
            "contents": list(map(lambda x: x.format_line(), self.children))
        }