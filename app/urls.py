from django.urls import path
from .views import *

urlpatterns = [
    path('home/', index_view, name='home'),
    path('detail <str:name>/', detail_view, name='detail_view')
]