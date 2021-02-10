from django import forms

class ContactForm(forms.Form):
	fullname = forms.CharField(label='Full name', max_length=30, required=True)
	subject = forms.CharField(label='Subject', max_length=30, required=True)
	email = forms.EmailField(label='Email', max_length=30, required=True)
	message = forms.CharField(label='Message', required=True, widget=forms.Textarea)
