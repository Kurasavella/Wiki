from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page>/", views.page, name='page'),
    path("serch/", views.serch, name='serch'),
    path("random/", views.random, name='random'),
    path("new_page/", views.new_page, name='new_page'),
    path("wiki/<str:pageHead>/edit/", views.edit_page, name='edit_page')
]
