from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
def helloView(reguest):
    return HttpResponse('<h1>Hello!It is my project</h1>')
def now_dateView(reguest):
    data11 = datetime.now().date()
    return HttpResponse(data11)
def goodbyView(reguest):
    return HttpResponse('<h1> Goodby user! </h1>')