from django.forms import ModelForm
from django.forms import Textarea 
from envaya.models import *

class BasicRuleForm(ModelForm):
	class Meta:
		model = BasicRule
		"""widgets = {
			'in_text' : Textarea(attrs={'cols': 10, 'rows': 20}),
			'out_text' : Textarea(attrs={'cols': 50, 'rows': 20}),
		}"""