from django.http import HttpResponse
from django.shortcuts import render


animals = [
    {
        "id": 0,
        "name": "Gryphon",
        "description": "Half egale half lion",
    },
    {
        "id": 1,
        "name": "Cthulu",
        "description": "High Priest of the ones beyond the stars",
    },
    {
        "id": 2,
        "name": "Werewolf",
        "description": "A man cursed into a bestial form",
    },
    {
        "id": 3,
        "name": "Centaur",
        "description": "Half horse, half human",
    },
    {
        "id": 4,
        "name": "Kraken",
        "description": "A giant murderous squid-thing",
    }
]


def home(request):
    data = { "animals": animals}
    return render(request, "home.html", data)


def show(request, id):
    matching_animals = [x for x in animals if x["id"] == id]
    # another way:
    # matching_animals = []
    # for animal in animals:
    #     if animal["id"] == id:
    #         matching_animals.append(animal)
    return HttpResponse(f"You're inspecting the {matching_animals[0]['name']}!")


def about(request):
    return HttpResponse("<h1>About</h1><p>We stock animals that shouldn't exist!</p>")


def meals(request):
    return HttpResponse("<h1>Meals</h1><p>You made the meals page!</p>")


def meals_eaten(request, id):
    matching_animals = []
    for animal in animals:
        if animal["id"] == id:
            matching_animals.append(animal)
    return HttpResponse(f"The {matching_animals[0]['name']} animal eats mice for breakfast!")
