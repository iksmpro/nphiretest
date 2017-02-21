import asyncio
from abc import abstractmethod, abstractproperty, ABC, ABCMeta

from . import Logger

class ExtendedABCMeta(ABCMeta):
    '''
    This extended metaclass created only with one purpose:
    We need to map all pairs name:class for all subclasses of the AbstractHandler.
    '''
    def __new__(mcls, name, bases, namespace):
        cls = super(ExtendedABCMeta, mcls).__new__(mcls, name, bases, namespace)
        handler_name = namespace.get('handler_name')
        # print('new subclass %s'%handler_name)
        if isinstance(handler_name, str) and handler_name not in AbstractHandler._subclass_names.keys():
            AbstractHandler._subclass_names[handler_name] = cls
        return cls

class AbstractHandler(ABC, metaclass=ExtendedABCMeta):
    """
    Abstract class to specify sms-handler class.
    DO NOT OVERWRITE send method.
    When you write your personal sms-handler class, all you need is
    overwrite send_message method and specify special handler_name.
    You can add extra functionality (more fields and methods),
    moreover you can add xml section handler name="{handler_name}" in XML
    config file. All XML parameters will be added to Class instance
    when object will be initialized.
    result object will contains information about this sms
    """
    @abstractproperty
    def handler_name(self):
        '''
        In real class instances (not abstact) you must to
        redefine it as field (not as method).
        Furthermore, it must be str instance.
        Definition should look something like this:
            class RealClass(AbstractHandler):
                handler_name = 'real_class'
                ...
        '''
        pass

    @abstractmethod
    async def send_message(self, phone, message) -> dict:
        '''
        All real functionality goes here. This method must be async.
        '''
        pass

    _subclass_names = dict()

    async def send(self, user_data) -> dict:
        '''
        do not overwrite it.
        This method used for sending sms. It just calling send_message method,
        but logging result in database.
        '''
        phone, message = user_data['phone'], user_data['message']
        self.result = {'status': 'ok', "message": 'PENDING'}
        result = await self.send_message(phone, message)
        self.result = result
        status, phone = result.get('status'), result.get('phone')
        if status == 'ok':
            Logger.log('SMS to %s has been sent.'%phone)
        elif status == 'error':
            error_tpl = result.get('error_code'), result.get('error_msg')
            Logger.log('Fail to send sms with code %s and message: %s'%error_tpl)
        return result
