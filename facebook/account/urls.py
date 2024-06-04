from django.urls import path
from .import views

urlpatterns = [
    path('task1/',views.task1),
    path('task2/<str:father>/<str:son>/',views.task2),
    path('fruit/',views.fruit),
    path('nav/',views.nav),


]
