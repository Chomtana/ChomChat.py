from ChomChat.Outputer.GlobalRegister import register_with_queue, register_without_queue


def RegisterOutputerWithoutQueue(provider_name):
    def wrap(f):
        register_without_queue(provider_name, f)
        return f
    return wrap


def RegisterOutputerWithQueue(provider_name):
    def wrap(f):
        register_with_queue(provider_name, f)
        return f
    return wrap