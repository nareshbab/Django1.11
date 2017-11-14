import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Restaurant
# Create your views here.
#function based views
# def home(request):
# 	return HttpResponse("Hello World")
# 	#return render(request, "home.html", {})#response

# class HomeView(TemplateView):
# 	template_name = 'home.html'

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(HomeView, self).get_context_data(*args, **kwargs)
# 		print(context)
# 		num = None
# 		some_list = [
# 			random.randint(0,100000), 
# 			random.randint(0,100000), 
# 			random.randint(0,100000)
# 		]
# 		condition_bool_item = True
# 		if condition_bool_item:
# 			num = random.randint(0,100000)
# 		context = {
# 			"bool_item": True,
# 			"num": num,
# 			"some_list": some_list
# 		}
# 		return context

# class ContactView(TemplateView):
# 	template_name = 'contact.html'

# class AboutView(TemplateView):
# 	template_name = 'about.html'

def restaurant_listview(request):
	template_name = 'restaurants/restaurants.html'
	restaurant_list = Restaurant.objects.all()
	context = {
		"restaurant_list": restaurant_list
	}
	return render(request, template_name, context)



















