from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.contact_list,name='contact_list'),
    path('<int:id>',views.contact_retrieve,name='contact_retrieve'),
    path('add/',views.contact_add,name='contact_add')
   
]