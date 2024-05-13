from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render


def NONE_indexed(request: HttpRequest):
    return render(request, 'fish_web_service/example.html')


def main_page(request: HttpRequest):
    return render(request, 'fish_web_service/main.html')


def fish_templates(request: HttpRequest, fish_id):
    data = {"fish_id": fish_id, "fish_name": ""}
    if fish_id == 1:
        data["fish_name"] = "Карп"
    elif fish_id == 2:
        data["fish_name"] = "Не карп"
    else:
        data["fish_name"] = "Другой не карп"
    return render(request, 'fish_web_service/fish-1.html', context=data)


def master_classes(request: HttpRequest):
    return render(request, 'fish_web_service/master-classes.html')


def master_classes_templates(request: HttpRequest, mk_id):
    return render(request, 'fish_web_service/example.html')


def search_fish(request: HttpRequest):
    context = {"fishes": None}
    template = 'fish_web_service/search-fish.html'
    if request.method == "POST":
        req_dict = request.POST.dict()
        data
        context["documents"] = function.get_documents(req_dict)

    return render(request, template, context)


def registration(request: HttpRequest):
    return render(request, 'fish_web_service/reg.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('fish_web_service/page-not-found.html')
