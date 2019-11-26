from django.shortcuts import render

from .forms import ContactForm

def contact(request):
	form = ContactForm()

	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			form.save()

	context = {'form' : form}

	return render(request, 'pages/home.html', context)