from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("hello")
    # param = {'name':'suraj','location':'odisha'}
    return render(request,'index.html')

def about(request):
    return HttpResponse("about")

def contact(request):
    return HttpResponse("contact")

def blog(request):
    djtext = request.GET.get('text', 'default')
    remove = request.GET.get('remove', 'off')
    print(djtext)
    print(remove)
    # analyzed = djtext
    if remove == "on":
        punctuations = '''!()-[]{};:'"\|/?!@#$%^&*<>,._~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed +char
        param = {'purpose':'Remove by Blog', 'analyzed_text': analyzed}
        return render(request, "analyze.html",param)
    else:
        return HttpResponse("Error")

def details(request):
    return HttpResponse("details")