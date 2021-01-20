from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'simulator/index.html')


def laughs(request):
    array = [
        'Robertinho', 'Canella', 'Laura Seraphim', 'Lucas Inutilismo'
    ]
    return render(request, 'simulator/laughs.html', {
        "nossers": sorted(array),
        "audios": [x for x in range(10)]
    })


def add_laugh(request):
    return render(request, 'simulator/addLaugh.html')