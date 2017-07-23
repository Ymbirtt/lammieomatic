class BaseLayout(object):
    @classmethod
    def render(cls, items):
        raise NotImplementedError
