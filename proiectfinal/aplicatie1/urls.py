

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create_post_actuals', views.create_post_actuals, name='create_post_actuals'),
    path('create_post_planning', views.create_post_planning, name='create_post_planning'),
    path('actuals',views.actuals, name='actuals'),
    path('planning',views.planning, name='planning'),

]
