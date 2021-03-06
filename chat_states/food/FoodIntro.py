from ChomChat import ChatState, Context
from ChomChat.Decorator import RegisterChatState
from outputer.actions.LinkAction import LinkAction
from outputer.actions.MessageAction import MessageAction
from outputer.basic.Button import Button
from outputer.basic.CardBasic import CardBasic
from outputer.basic.Text import Text


@RegisterChatState("food_intro")
class FoodIntro(ChatState):
    def __init__(self, context: Context):
        # Code here

        super().__init__(context)

    def on_enter(self, from_: ChatState, args, is_interrupt: bool):
        # Code here
        self.context.outputer.send(CardBasic(
            title='กินไรยัง ?',
            footer=[
                Button("ซื้อข้าวกินมาแล้ว", MessageAction("ซื้อข้าวกินมาแล้ว")),
                Button("ทำกินเองที่บ้าน", MessageAction("ทำกินเองที่บ้าน")),
                Button("มีคนเลี้ยง", MessageAction("มีคนเลี้ยง")),
                Button("ยังไม่ได้กินเลย", MessageAction("ยังไม่ได้กินเลย")),
            ]
        ))

        super().on_enter(from_, args, is_interrupt)

    def on_message(self, message: str):
        # Code here
        if message == "ทำกินเองที่บ้าน": self.context.next("food_self")
        super().on_message(message)

    def on_finish(self, args):
        # Code here

        super().on_finish(args)

    def on_next(self, to: ChatState, args):
        # Code here

        super().on_next(to, args)

    def on_return(self, from_: ChatState, args):
        # Code here

        super().on_return(from_, args)

    def before_interrupt(self, by: ChatState, args):
        # Code here

        super().before_interrupt(by, args)

    def after_interrupt(self, by: ChatState, args):
        # Code here

        super().after_interrupt(by, args)

