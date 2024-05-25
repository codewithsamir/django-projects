from django.shortcuts import render
from . models import NewData
# Create your views here.
def code(request):
    codeshow  = NewData.objects.all
    return render(request, "code/all_code.html", {"newthing": codeshow})

