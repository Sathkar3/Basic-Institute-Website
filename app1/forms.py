from  django import forms


class ContactForm(forms.Form):

	NAME = forms.CharField(max_length=20)

	PHONE = forms.IntegerField()

	EMAIL = forms.EmailField()

	MESSAGE = forms.CharField(max_length=100)