from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic import CreateView, DeleteView
from .forms import WidgetForm


# Create your views here.
def index(request):
    widget_list = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, "index.html", {"widget_list": widget_list, "widget_form": widget_form})

def add_widget(request):
    form = WidgetForm(request.POST)
    form.save()
    return redirect("index")