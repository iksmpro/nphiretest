from .abstracthandler import AbstractHandler
from .config_class import ConfigClass

def get_handler(handler_name: str) -> AbstractHandler:
    cls = AbstractHandler._subclass_names.get(handler_name)
    if cls:
        instance = cls()
        params = ConfigClass.get_params(handler_name)
        if params:
            instance.__dict__.update()
        return instance
    else:
        raise LookupError("No such handler with name %s"%handler_name)