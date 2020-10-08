from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>', views.detail, name='topic'),
    path('Weightage/Standard', views.weightage, name='weightage'),
    path('About/Standard', views.About, name='about'),
   ]
