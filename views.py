from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import RequestContext, render_to_response
from django.template import loader
from random import choice


from envaya.forms import *

def home(request):
	"""root page for envaya : where all the rules are processed"""
	
	if request.method == 'POST':
		answers = [
				"It is certain","It is decidedly so", "Without a doubt",
                "Yes - definitely", "You may rely on it", "As I see it, yes",
                "Most likely", "Outlook good", "Yes", "Signs point to yes",
                "Reply hazy, try again", "Ask again later", "Better not tell you now",
                "Cannot Predict now", "Concentrate and ask again", "Don't count on it",
                "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
		mess="hahahaha"        
		#if request.POST["action"] in ["incoming"]:
		return render_to_response('envaya/index.json' , {'var':mess, 'phone':request.POST["from"]}, mimetype="application/json" )
		#else:
		return render_to_response('envaya/log.json' , {'var':request.POST}, mimetype="application/json")


def admin(request):
	"""admin page : where all the rules are set"""

	return render_to_response('envaya/admin.html' , {'IncomingForm':IncomingForm, 'SendForm':SendForm})
