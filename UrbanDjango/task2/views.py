from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func_template(request):
    return render(request, 'func_template.html')

def hello(request):
    return render(request, 'hello.html')

class class_template(TemplateView):
    template_name = 'class_template.html'