from ChomChat.ChomChat import global_chom_chat


def RegisterChatState(name):
    def wrap(chat_state_class):
        chat_state_class.name = name
        global_chom_chat.register_chat_state(name, chat_state_class)
        return chat_state_class
    return wrap


def RegisterContextBuilder(provider_name):
    def wrap(f):
        global_chom_chat.register_context_builder(provider_name, f)
        return f
    return wrap


def RegisterContextGetter(provider_name):
    def wrap(f):
        global_chom_chat.register_context_getter(provider_name, f)
        return f
    return wrap
