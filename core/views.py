from django.shortcuts import render, HttpResponse

# Create your views here.
def ola(request,nome,idade):
    return HttpResponse('<H1>Alo {} de {} anos</h1>'.format(nome,idade))
