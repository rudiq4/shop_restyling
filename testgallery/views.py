from django.shortcuts import render
from .models import Test


def general(request):
    template = 'test/test.html'
    kartinki = Test.objects.all()
    context = {'kartinki': kartinki}
    return render(request, template, context)
