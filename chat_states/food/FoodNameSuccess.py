from ChomChat import ChatState, Context
from ChomChat.Decorator import RegisterChatState
from outputer.actions.MessageAction import MessageAction
from outputer.basic.Button import Button
from outputer.basic.CardBasic import CardBasic
from outputer.basic.Text import Text


@RegisterChatState("food_name_success")
class FoodNameSuccess(ChatState):
    def __init__(self, context: Context):
        # Code here

        super().__init__(context)

    def on_enter(self, from_: ChatState, args, is_interrupt: bool):
        # Code here
        self.context.outputer.send(CardBasic(
            title='เย้ !',
            body=Text('จด '+self.context.state.record.name+' '+str(self.context.state.record.value)+' บาท เรียบร้อยแล้ว')
        ))
        self.context.next('food_finish')
        super().on_enter(from_, args, is_interrupt)

    def on_message(self, message: str):
        # Code here
        #if message == 'จด': self.context.next("food_name")
        #if message == 'ไม่บอก': self.context.next("food_finish")
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

