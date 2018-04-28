from django.shortcuts import render, HttpResponse, redirect
import datetime, time

def index(request):
    if 'wordlist' not in request.session:
        request.session['wordlist'] = []
    return render(request,"session_word/index.html")

def add_word(request):
    content = {'word': request.POST['word'],
                'time': time.strftime("%b %d,%Y %I:%M %p"),
                'color':request.POST['color'],
                'size':request.POST['size']
    }
    request.session['wordlist'].append(content)
    request.session.modified = True
    print content
    return redirect('/session_word')

def clear(request):
    request.session.clear()
    return redirect('/session_word')
    
# Create your views here.
