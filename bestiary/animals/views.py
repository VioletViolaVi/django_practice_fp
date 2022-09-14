from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Animal


def home(request):
    data = {"animals": Animal.objects.all()}  # like '*' select all selector
    return render(request, "home.html", data)


def show(request, id):
    animal = get_object_or_404(Animal, pk=id)
    # one way:
    # matching_animals = [x for x in animals if x["id"] == id]
    # another way:
    # matching_animals = []
    # for animal in animals:
    #     if animal["id"] == id:
    #         matching_animals.append(animal)
    return render(request, "animal.html", {"animal": animal})


def about(request):
    return HttpResponse("<h1>About</h1><p>We stock animals that shouldn't exist!</p>")


def not_found_404(request, exception):
    data = {"error": exception}
    return render(request, "404.html", data)


# i did the below:

def meals(request):
    return HttpResponse("<h1>Meals</h1><p>You made the meals page!</p>")


def meals_eaten(request, id):
    matching_animals = []
    for animal in animals:
        if animal["id"] == id:
            matching_animals.append(animal)
    return HttpResponse(f"The {matching_animals[0]['name']} animal eats mice for breakfast!")
