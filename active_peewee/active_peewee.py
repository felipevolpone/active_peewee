
class ActiveMeta(type):

    def __getattr__(self, method_name):
        def inner(*args, **kwargs):
            return method_name

        inner.__name__ = method_name
        return inner


class ActivePeewee(object):
    __metaclass__ = ActiveMeta

    # the idea is Peewee models inhenrit this class to provide
    # the activepeewee features to their models
