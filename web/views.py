from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404,render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required
def index(request):
	return render_to_response('web/index.html',{})

@csrf_exempt
def fblogin(request):
	print '*********',request.POST['fbid']
	request.session['fbid'] = request.POST['fbid']
	return HttpResponse("true")
