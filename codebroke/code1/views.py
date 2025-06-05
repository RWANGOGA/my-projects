from django.shortcuts import render , HttpResponse

# Create your views here.
def code1home(index):
    return HttpResponse("code1Home page")

def code1contact(index):
    return HttpResponse("Contact page")
def code1about(index):
    return HttpResponse("About page")
def code1post(request,slug):
    return HttpResponse(f"This is a  code1post: {slug} ")
