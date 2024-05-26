from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FishForm
from .models import Fish
import os
import json

def NONE_indexed(request: HttpRequest):
    return render(request, 'fish_web_service/example.html')

def main_page(request: HttpRequest):
    return render(request, 'fish_web_service/main.html')

def fish_templates(request: HttpRequest, fish_id):
    fish_data = list(Fish.objects.filter(id=fish_id).values())[0]
    template = f'fish_web_service/fish-templates/fish-{fish_data["photos_count"]}.html'
    return render(request, template, context=fish_data)

def master_classes(request: HttpRequest):
    return render(request, 'fish_web_service/master-classes.html')

def origami(request: HttpRequest):
    return render(request, 'fish_web_service/origami.html')

def master_classes_templates(request: HttpRequest, mk_id):
    return render(request, 'fish_web_service/example.html')

def search_fish(request: HttpRequest):
    context = {"fishes": None}
    template = 'fish_web_service/search-fish.html'
    if request.method == "POST":
        req_dict = request.POST.dict()
        fishes_data = list(Fish.objects.filter(name__icontains=req_dict.get('fish_name')).values())
        context["fishes"] = fishes_data
    return render(request, template, context)


def add_fish(request):
    if request.method == 'POST':
        fish_form = FishForm(request.POST, request.FILES)
        if fish_form.is_valid():
            fish = fish_form.save(commit=False)
            images = request.FILES.getlist('images')
            if len(images) != fish.photos_count:
                return render(request, 'fish_web_service/fish-templates/add_fish.html', {
                    'fish_form': fish_form,
                    'error': 'Number of images does not match photos_count'
                })
            fish.save()  # Save the fish object first to get an ID

            image_paths = []
            fish_folder = os.path.join('static/fish_web_service/images/fish-template', str(fish.id))
            if not os.path.exists(fish_folder):
                os.makedirs(fish_folder)

            for index, image in enumerate(images):
                image_filename = os.path.join(fish_folder, f'{index + 1}.jpg')
                with open(image_filename, 'wb+') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)
                image_paths.append(f'{index + 1}.jpg')

            fish.image_paths = json.dumps(image_paths)
            fish.save()  # Save the fish object with updated image paths
            return redirect('fish_web_service:fish_detail', pk=fish.pk)
    else:
        fish_form = FishForm()
    return render(request, 'fish_web_service/fish-templates/add_fish.html', {'fish_form': fish_form})

def fish_detail(request, pk):
    fish = get_object_or_404(Fish, pk=pk)
    fish.image_paths = json.loads(fish.image_paths)
    return render(request, 'fish_web_service/fish-templates/fish_detail.html', {'fish': fish})

def registration(request: HttpRequest):
    return render(request, 'fish_web_service/reg.html')

def page_not_found(request, exception):
    return HttpResponseNotFound('fish_web_service/page-not-found.html')
