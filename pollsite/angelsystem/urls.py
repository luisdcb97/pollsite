from django.urls import path

from . import views

app_name = 'angelsystem'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tree', views.tree, name='tree'),
]
