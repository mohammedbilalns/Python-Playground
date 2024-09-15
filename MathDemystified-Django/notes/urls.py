from django.urls import path
from .import views

app_name = 'notes'
urlpatterns = [
    path('', views.notes_list, name="list"),
    path('plusone/', views.plusone, name="plusone"),
    path('plustwo/', views.plustwo, name="plustwo"),
    path('linearalgebra/', views.linearalgebra, name="linearalgebra"),
    path('<slug:slug>', views.notespage, name="page"),


  
]
