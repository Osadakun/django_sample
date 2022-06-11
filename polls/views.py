from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

def index(request):
  return render(request, 'polls/menu1.html')

def submit_order(request):
  return render(request, 'polls/set_order_view.html')

def login(request):
  return render(request, 'polls/login_view.html')

def confirm(request):
  return render(request, 'polls/confirm_order_view.html')

def detail(request):
  return render(request, 'polls/order_detail.html')
