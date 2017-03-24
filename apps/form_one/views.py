from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):

    return render(request, 'form_one/index.html')

def process(request):

    if request.session.get('submissions', default=None) == None:
        request.session['submissions'] = 0
    if request.method == "POST":
        request.session['submissions'] += 1
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['description'] = request.POST['description']

    return redirect('/results')


def results(request):

    if request.method == "GET":

        context = {
        'submissions' : request.session['submissions'],
        'name' : request.session['name'],
        'location' : request.session['location'],
        'language' : request.session['language'],
        'description' : request.session['description']
        }

    return render(request, 'form_one/results.html', context)
