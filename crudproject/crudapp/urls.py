from django.urls import path
from crudapp import views
urlpatterns = [
    path('', views.index, name='index'),
     path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:crudid>/',views.delete,name="delete"),
]
