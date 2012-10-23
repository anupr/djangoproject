from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.views import redirect_to_login

def login_required(fun):
	def new_f(request):
		path = request.get_full_path()
		try:
			if request.user.is_authenticated():
				return fun(request)
			else:
				if request.session['fbid'] :
					return fun(request)
				else:
					return redirect_to_login(path, '/accounts/login/')
		except KeyError:
			return redirect_to_login(path, '/accounts/login/')

	return new_f
