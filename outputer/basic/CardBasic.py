from typing import List
from ChomChat.Outputer import Component
from config import NEW_MESSAGE_DEFAULT_TEXT
from outputer.basic.Text import Text


class CardBasic(Component):
    name: str = 'CardBasic'
    title: str
    body: Component
    footer: List[Component]
    header: Component
    alt_text: str

    def __init__(self, title: str = None, body: Component = None, footer: List[Component] = [], header: Component = None, alt_text: str = None):
        self.title = title
        self.body = body
        self.footer = footer
        self.header = header

        if alt_text is None:
            if title is not None: alt_text = title
            elif isinstance(body, Text): alt_text = body.message
            else: alt_text = NEW_MESSAGE_DEFAULT_TEXT

        self.alt_text = alt_text

    def format_line(self):
        result = {
            "type": "bubble"
        }

        if self.header is not None:
            result['hero'] = self.header.format_line()

        if self.title is not None or self.body is not None:
            result['body'] = {
                "type": "box",
                "layout": "vertical",
                "contents": []
            }

            if self.title is not None:
                result['body']['contents'].append({
                    "type": "text",
                    "text": self.title,
                    "weight": "bold",
                    "size": "xl"
                })

            if self.body is not None:
                result['body']['contents'].append({
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": [
                        self.body.format_line()
                    ]
                })

        if len(self.footer) > 0:
            result['footer'] = {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [],
                "flex": 0
            }

            for footer in self.footer:
                result['footer']['contents'].append(footer.format_line())

            result['footer']['contents'].append({
                "type": "spacer",
                "size": "sm"
            })

        return {
            "type": "flex",
            "altText": self.alt_text,
            "contents": result
        }
