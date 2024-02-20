from django.urls import path
from firsttry import views

urlpatterns = [
    # for home or main page
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('Home/',views.home,name='home'),
    path('index/',views.home,name='home'),

    # for CRUD (create, read, update, delete)
    path('delete/<id>',views.delete, name = 'delete'),
    path('create/',views.create, name='create'),
    path('edit/<id>',views.edit, name='edit'),
]