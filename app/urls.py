from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name = 'index_view'),
    path("detail_view/<str:name>/", detail_view, name = 'detail_view'),
    path('add_car/', add_car, name = 'add_car'),
    path('delete_car/<int:car_id>/', delete_car, name = 'car_deletion'),
    path('edit_car/<int:car_id>/', edit_car, name = 'edit_car'),
]