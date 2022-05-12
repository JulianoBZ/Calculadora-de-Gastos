from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class FormularioView(TemplateView):
    template_name = "formulario.html"

def formreq(request):
    if request.method=="POST":
        print("Postado")
    return render (request, 'formulario.html')