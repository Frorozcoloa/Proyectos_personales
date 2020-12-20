from django.shortcuts import render
from django.http import HttpResponse

def cookie(request):
    resp = HttpResponse('<ul><li><p><a href="/polls">da0b1b5b</a></p></li></ul>')
    resp.set_cookie ('dj4e_cookie', 'da0b1b5b', max_age = 1000)
    return resp

def hello(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4: del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    resp.set_cookie ('dj4e_cookie', 'da0b1b5b', max_age = 1000)
    return resp