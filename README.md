# nphiretest
Do not forget to makemigrations and migrate. Then start the server.
***
I have to used Python 3.6.
***
One more thing: a have to make two caps for smsc and smstraffic. They dont really work, because this is not a part of test task, I guess.
***
###USAGE:

```
def snd():
    r = requests.post('http://127.0.0.1:8000/sendsms/', data={'phone':'79990000000','message':'take me to church', 'handler_name':'smsc-handler'})
    return r.json()['handler']
def gtr(h):
    r2 = requests.get('http://127.0.0.1:8000/getstatus/?handler=%s'%h)
    print(r2, r2.text)
h = snd()
gtr(h)
```