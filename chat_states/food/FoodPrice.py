from ChomChat import ChatState, Context
from ChomChat.Decorator import RegisterChatState
from outputer.actions.LinkAction import LinkAction
from outputer.actions.MessageAction import MessageAction
from outputer.basic.Button import Button
from outputer.basic.CardBasic import CardBasic
from outputer.basic.Text import Text


@RegisterChatState("food_price")
class FoodPrice(ChatState):
    def __init__(self, context: Context):
        # Code here

        super().__init__(context)

    def on_enter(self, from_: ChatState, args, is_interrupt: bool):
        # Code here
        self.context.outputer.send(CardBasic(
            title='ใช้เงินไปกี่บาทเอ่ย ?',
            body=Text('พิมพ์จำนวนเงิน ที่ใช้ซื้ออาหาร และ เครื่องดื่ม'),
            footer=[
                Button("เมื้อกี้กดผิด", MessageAction("เมื้อกี้กดผิด")),
                Button("ไม่อยากบอกแล้ว", MessageAction("ไม่อยากบอกแล้ว"))
            ]
        ))

        super().on_enter(from_, args, is_interrupt)

    def on_message(self, message: str):
        # Code here
        if message == "เมื้อกี้กดผิด": self.context.next("food_intro")
        elif message == "ไม่อยากบอกแล้ว": self.context.next("food_intro")
        else:
            self.context.state.record.value = message
            self.context.next("food_price_success")
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

