from django.http import HttpResponse
from django.utils import simplejson
from browserinfo.models import BrowserInfo
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def detect_info(request):

    class BrowserInfoForm(ModelForm):
        class Meta:
            model = BrowserInfo
            exclude = ('user',)

    if request.method != 'POST' or not request.is_ajax():
        return render_to_response('browserinfo/browserinfo.html', context_instance=RequestContext(request))


    form = BrowserInfoForm(request.POST)


    if form.is_valid():
        info = form.save(commit=False)
        info.user = request.user
        info.user_agent = request.META.get('HTTP_USER_AGENT', None)
        info.ip = request.META.get('REMOTE_ADDR', None)
        info.save()
        
        return HttpResponse(
                            simplejson.dumps({
                                                'success':True, 
                                                'pk':info.pk,                                                      
                                                }),
                            mimetype='application/json'
                            )
        
    
    return HttpResponse(
                            simplejson.dumps({
                                                'success':False, 
                                                'errors':form.errors,                                                    
                                                }),
                            mimetype='application/json'
                            )

