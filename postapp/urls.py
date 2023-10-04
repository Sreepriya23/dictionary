from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>/', views.get_detail_by_id, name='get_detail_by_id'),
    path('detail/', views.get_detail_by_id, name='get_detail_by_id'),

]
