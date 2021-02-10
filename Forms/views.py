from django.shortcuts import render, redirect

from django.http import JsonResponse

from .forms import ContactForm

from .models import Contact, Users

import logging

# Create your views here.
def forms(request):
	if processRequest(request):

			return redirect('/forms/?processed=true')

	contactForm = ContactForm()

	senders = getSenders()

	return render(request, 'forms.html', {
		'page': {
			'title': 'Services page',
			'scripts': [
				'/static/js/forms.js'
			],
		},
		'pageData': {
			'senders': senders
		},
		'regularContactForm': contactForm,
	})




#ajax handler
def ajax(request):
	data={'result':'ERROR','msg':'Error 1001'}

	if processRequest(request):
		data['result']='OK'
		data['msg']='Message successfully received'
		data['senders']=getSenders()

	return JsonResponse(data)


#common function
def processRequest(request):
	result = False;
	if request.method == 'POST':
		#form
		cf = ContactForm(request.POST)
		if cf.is_valid():
			#storing data
			reg = Contact(fullname=cf.cleaned_data['fullname'], subject=cf.cleaned_data['subject'], email=cf.cleaned_data['email'], message=cf.cleaned_data['message'])
			reg.save()

			result = True

	return result

def getSenders():
	return list(Contact.objects.all().values())
