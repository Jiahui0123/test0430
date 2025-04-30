from django.shortcuts import render, get_object_or_404

# Create your views here.
from flower.models import Flower

def flowers(request):
    q = request.GET.get('q', None)
    flowers = ''
    if q is None or q is "":
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)
    return render(request, 'flower/flower.html', {'flowers': flowers })
    # flowers = Flower.objects.all()
    # return render(request, 'flower/flower.html', {'flowers': flowers})

def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'flower/detail.html', locals())
