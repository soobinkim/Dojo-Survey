from django.shortcuts import render, redirect

def index(request):
    if request.session.get('count') == None:
        request.session['count'] = 0
    return render(request,'surveyForm/index.html')



def results(request):
    if request.method == 'POST':
        request.session['username'] = request.POST['username']
        request.session['locations'] = request.POST['locations']
        request.session['languages'] = request.POST['language']
        request.session['count'] += 1
    return render(request, 'surveyForm/results.html')

def back(request):
    return render(request,'surveyForm/index.html')


# Create your views here.
