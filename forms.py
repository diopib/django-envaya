from django.forms import ModelForm 
from envaya.models import *

class IncomingForm(ModelForm):
	class Meta:
		model = Incoming

class SendForm(ModelForm):
	class Meta:
		model = Send