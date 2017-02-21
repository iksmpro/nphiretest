import asyncio
from time import time

from .smshandlers import get_handler

class AsyncManager:
    def __init__(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.hash_table = dict()  # maybe we should do it in DB, but fts

    def do_stuff(self):
        self.loop.run_forever()

    def send_sms(self, handler_name, userdata):
        sms_handler = get_handler(handler_name)
        hash_value = "%s-%s" % (hash(sms_handler),userdata['phone'])
        self.hash_table[hash_value] = [sms_handler, time()]
        self.loop.call_soon_threadsafe(asyncio.async, sms_handler.send(userdata))
        return hash_value

    def get_status(self,hash_value):
        lst = self.hash_table.get(hash_value)
        if isinstance(lst,list):
            result = getattr(lst[0], 'result', None)
            if not result:
                return {'status': 'error', "message": "UNEXPECTED ERROR"}
            if lst[1] + 86400 < time():
                self.hash_table.pop(hash_value, None)
                return {'status': 'error', "message": "EXPIRED"}
            return result
        return {'status': 'error', "message": 'NOT EXIST'}
