from django.utils import timezone
# import logging
# from time import ctime

module = __import__('.'.join(__package__.split('.')[:-1]))
LogObject = module.models.LogObject

class Logger:
    @classmethod
    def log(cls,messsage):
        LogObject.objects.create(time=timezone.now(), text=messsage)
        # logging.basicConfig(filename='logfile.log',level=logging.DEBUG)
        # logging.logit = lambda msg: logging.info('%s at %s'%(msg,ctime()))

