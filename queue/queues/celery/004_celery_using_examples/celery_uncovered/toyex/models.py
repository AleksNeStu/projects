class Repository(object):
    def __init__(self, obj):
        """
        The __init__ function is called when a new instance of the class is created.
        It takes one argument, self, which refers to the object itself.
        The __init__ function sets up any attributes that are required for the object's state.

        :param self: Refer to the object itself
        :param obj: Store the object that is being wrapped
        :return: The object that is being wrapped
        :doc-author: Trelent
        """
        self._wrapped_obj = obj
        self.language = obj[u'language'] or u'unknown'
        self.name = obj[u'full_name']

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        else:
            return getattr(self._wrapped_obj, attr)
