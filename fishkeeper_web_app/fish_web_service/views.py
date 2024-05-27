from django.http import HttpRequest, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
import os

from fish_web_service.models import Fishes


def NONE_indexed(request: HttpRequest):
    return render(request, 'fish_web_service/example.html')


def main_page(request: HttpRequest):
    return render(request, 'fish_web_service/main.html')


def fish_templates(request: HttpRequest, fish_id):
    fish_data = list(Fishes.objects.filter(id=fish_id).values())[0]
    if fish_data is not None:
        template = f'fish_web_service/fish-templates/fish-{fish_data["photos_count"]}.html'
        return render(request, template, context=fish_data)
    else:
        return HttpResponseRedirect('search-fish')


def add_fishes(request: HttpRequest):
    fish_data = {}
    template = 'fish_web_service/add_fishes.html'
    if request.method == "POST":
        req_dict = request.POST.dict()
        Fishes.objects.create(name=req_dict.get('name'),
                              type=req_dict.get('type'),
                              description=req_dict.get('description'),
                              habitat=req_dict.get('habitat'),
                              requirements=req_dict.get('requirements'),
                              food=req_dict.get('food'),
                              photos_count=req_dict.get('photos_count')
                              )
        fish_id = list(Fishes.objects.filter(name=req_dict.get('name'), type=req_dict.get('type')).values())[0]['id']
        fish_folder = os.path.join('static/fish_web_service/images/fish-template/', str(fish_id))
        if not os.path.exists(fish_folder):
            os.makedirs(fish_folder)
        """for index, image in enumerate(images):
            image_filename = os.path.join(fish_folder, f'{index + 1}.jpg')
            with open(image_filename, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)"""

    return render(request, template, context=fish_data)


def master_classes(request: HttpRequest):
    return render(request, 'fish_web_service/master-classes.html')


def origami(request: HttpRequest):  # Сделано для примера, нужно сделать такую же систему как с рыбами
    return render(request, 'fish_web_service/origami.html')


def programming(request: HttpRequest):  # Сделано для примера, нужно сделать такую же систему как с рыбами
    return render(request, 'fish_web_service/programming.html')


def master_classes_templates(request: HttpRequest, mk_id):
    return render(request, 'fish_web_service/example.html')


def search_master_classes(request: HttpRequest):
    return render(request, 'fish_web_service/search-mk.html')


def search_fish(request: HttpRequest):
    context = {"fishes": None}
    template = 'fish_web_service/search-fish.html'
    if request.method == "POST":
        req_dict = request.POST.dict()
        fishes_data = list(Fishes.objects.filter(name__icontains=req_dict.get('fish_name')).values())
        context["fishes"] = fishes_data
    else:
        context["fishes"] = list(Fishes.objects.all().values())

    return render(request, template, context)


def registration(request: HttpRequest):
    return render(request, 'fish_web_service/reg.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('fish_web_service/page-not-found.html')
