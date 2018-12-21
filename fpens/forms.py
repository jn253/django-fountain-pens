from django import forms

from .models import Pen

class Pen(forms.ModelForm):

	class Meta:
	
		model = Pen
