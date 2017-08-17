
import base_missile_model


class SimpleMissile(base_missile_model.BaseMissile):
    def __init__(self):
        base_missile_model.BaseMissile.__init__(self)


# The decorator of singleton class
def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton


@singleton
class ModelsManager(object):
    def __init__(self):
        self.model = None

    def set_model(self, model_name):
        if model_name is "SimpleMissile":
            self.model = SimpleMissile()

