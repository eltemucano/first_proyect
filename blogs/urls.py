from django.urls import path, include
from . import views
# En esta sección defines las redirecciones a la vista
urlpatterns = [
    path('blogs/new', views.new),
    path('blogs',views.index),
    path('blogs/create',views.create),
    path('blogs/<int:my_val>',views.show),
    path('blogs/<int:my_val>/edit',views.edit),
    path('blogs/<int:my_val>/delete',views.destroy),
    path('blogs/json',views.jsonView),
    path('',views.redirige)
]