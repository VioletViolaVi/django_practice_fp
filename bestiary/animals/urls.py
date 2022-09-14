# map view functions to url patterns

from hashlib import new
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="animals-home"),
    path("about/", views.about, name="animals-about"),
    path("show/<int:id>", views.show, name="animals-show"),
    path("meals/", views.meals, name="animals-meals"),
    path("meals-eaten/<int:id>", views.meals_eaten, name="animals-meals-eaten")
]
