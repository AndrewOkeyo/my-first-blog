from django.shortcuts import render
from django.http import HttpResponse

from django.template.loader import get_template
from django.template import Context, Template


# Create your views here.


def firstpage(request):
    t = get_template('index.html')
    return HttpResponse(t.render({'time': '12131'}))  

def index(request):
    t = get_template('events/index.html')
    return HttpResponse(t.render({}))
    #return render_to_response('events/index1.html')


def musician(request):
    MUSICIANS = [
	{'name': 'Django Reinhardt', 'genre': 'jazz'},
	{'name': 'Jimi Hendrix', 'genre': 'rock'},
	{'name': 'Louis Armstrong', 'genre': 'jazz'},
	{'name': 'Pete Townsend', 'genre': 'rock'},
	{'name': 'Yanni', 'genre': 'new age'},
	{'name': 'Ella Fitzgerald', 'genre': 'jazz'},
	{'name': 'Wesley Willis', 'genre': 'casio'},
	{'name': 'John Lennon', 'genre': 'rock'},
	{'name': 'Bono', 'genre': 'rock'},
	{'name': 'Garth Brooks', 'genre': 'country'},
	{'name': 'Duke Ellington', 'genre': 'jazz'},
	{'name': 'William Shatner', 'genre': 'spoken word'},
	{'name': 'Madonna', 'genre': 'pop'},
    ]
    t = get_template('events/musician.html')
    return HttpResponse(t.render({'musician': MUSICIANS}))

