from django.shortcuts import render

# Create your views here.


def login(request):
	template_name = 'user_management/login.html'
	context = {
		"user": ""
	}
	return render(request, template_name, context)