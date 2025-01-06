from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name='create_event'),
    path("get/<str:id>", views.getById, name='get_event'),
    path("update/<str:id>", views.updateById, name='update_event'),
    path("delete/<str:id>", views.deleteById, name='delete_event')

]