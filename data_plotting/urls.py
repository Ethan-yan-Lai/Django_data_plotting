from django.urls import path
from .views import generate_image
from . import views

urlpatterns = [
    path('generate-image/', views.generate_image, name='generate_image'),
    path('', views.generate_image, name='data_plotting_home'),
    path('link1/', views.link_1_view, name='link_1'),
    path('link2/', views.link_2_view, name='link_2'),
    path('link3/', views.link_3_view, name='link_3'),

]