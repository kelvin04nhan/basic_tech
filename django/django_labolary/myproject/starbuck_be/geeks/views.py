from django.shortcuts import render
from django.http import HttpResponse
from .forms import GeeksForm
# Create your views here.
def index(request):
    return HttpResponse("WELLCOME TO GEEK HOME")


def create_view(request):
    
    context = {}
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context['form'] = form
    return render(request, './geeks/create_view.html',context)
