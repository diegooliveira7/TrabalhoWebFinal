
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('estudante/<int:id>', estudante, name='estudante'),
]



