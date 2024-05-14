from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render

from fish_web_service.models import Fishes


def NONE_indexed(request: HttpRequest):
    return render(request, 'fish_web_service/example.html')


def main_page(request: HttpRequest):
    return render(request, 'fish_web_service/main.html')


def fish_templates(request: HttpRequest, fish_id):
    fish_data = list(Fishes.objects.filter(id=fish_id).values())[0]
    template = f'fish_web_service/fish-templates/fish-{fish_data["photos_count"]}.html'

    return render(request, template, context=fish_data)


def master_classes(request: HttpRequest):
    return render(request, 'fish_web_service/master-classes.html')


def origami(request: HttpRequest): # Сделано для примера, нужно сделать такую же систему как с рыбами
    return render(request, 'fish_web_service/origami.html')


def master_classes_templates(request: HttpRequest, mk_id):
    return render(request, 'fish_web_service/example.html')


def search_fish(request: HttpRequest):
    context = {"fishes": None}
    template = 'fish_web_service/search-fish.html'
    if request.method == "POST":
        req_dict = request.POST.dict()
        fishes_data = list(Fishes.objects.filter(name__icontains=req_dict.get('fish_name')).values())
        context["fishes"] = fishes_data

    return render(request, template, context)


def registration(request: HttpRequest):
    return render(request, 'fish_web_service/reg.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('fish_web_service/page-not-found.html')
