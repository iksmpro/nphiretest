from django.http import JsonResponse

from . import shared_object

def send_sms(request):
    '''
    send a post request with 'phone' 'message' and 'hanlder' (this is handler name) func to send an sms
    it will return "handler" parameter, which will contains id of your message. You can use it to check your   
    '''
    handler = request.POST.get('handler_name')
    if handler and request.POST.get('phone') and request.POST.get('message'):
        sms_handler_id = shared_object.manager.send_sms(handler,request.POST)
        return JsonResponse({'status':'ok','message':'this is your sms_handler', 'handler':sms_handler_id})
    else:
        return JsonResponse({'status':'error','message':'some of "handler_name", "phone" or "message" parameters not uncluded in post-request'})

def get_sms_status(request):
    '''
    use this to get sms_status: sended, expired, pending, etc. Specify 'handler' in get params.
    You must get 'handler' param form send_sms func
    '''
    handler = request.GET.get('handler')
    if handler:
        result = shared_object.manager.get_status(handler)
        return JsonResponse(result)
    else:
        return JsonResponse({'status':'error','message':'you have not specify handler'})
