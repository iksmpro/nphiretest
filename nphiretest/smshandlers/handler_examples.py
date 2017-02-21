import random
import asyncio
from .abstracthandler import AbstractHandler

# this two handlers are caps

class HandlerSMSC(AbstractHandler):
    handler_name = 'smsc-handler'

    async def send_message(self, phone, message) -> dict:
        if phone and message:
            # use api-keys (self.api_key)
            # send message to phone  # http://smsc.ru/some­api/message/
            await asyncio.sleep(random.randint(1,20))  # for example, it will be success
            return {'status': 'ok', 'phone': phone}
        else:
            return {'status': 'error', 'phone': phone, 'error_code': -3500, 'error_msg': 'Невозможно отправить сообщение указанному абоненту'}

class HandlerSMSTraffic(AbstractHandler):
    handler_name = 'smstraffic-handler'

    async def send_message(self, phone, message) -> dict:
        if phone and message:
            # send message to phone  # http://smstraffic.ru/super­api/message/
            await asyncio.sleep(random.randint(1,20))  # for example, it will be success
            return {'status': 'ok', 'phone': phone}
        else:
            return {'status': 'error', 'phone': phone, 'error_code': -3500, 'error_msg': 'Невозможно отправить сообщение указанному абоненту'}

   