from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import RequestContext, render_to_response
from django.template import loader
from random import choice
from forms import BasicRuleForm
from models import BasicRule


from envaya.forms import *

def home(request):
	"""root page for envaya : where all the rules are processed"""
	
	if request.method == 'POST':
		if request.POST["action"] in ["incoming"]:
			try:
				rule_to_apply = BasicRule.objects.get(in_text=request.POST["message"])
				return render_to_response('envaya/index.json' , {'message':rule_to_apply.out_text, 'to':request.POST["from"]},  mimetype="application/json" )
			except:
				pass
		
		


def admin(request):
	"""admin page : where all the rules are set"""

	if request.method == 'POST':
		form=BasicRuleForm(request.POST)
		if form.is_valid():
			form.save()

	form = BasicRuleForm()
	br = BasicRule.objects.all().order_by('-id')
	#return render_to_response('envaya/admin.html' , {'BasicRuleForm':form})

	t = loader.get_template('envaya/admin.html')
	c = RequestContext(request, {'BasicRuleForm':form, 'BasicRule':br})
	return HttpResponse(t.render(c))
