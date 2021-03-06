
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create_post_actuals', views.create_post_actuals, name='create_post_actuals'),
    path('create_post_planning', views.create_post_planning, name='create_post_planning'),
    path('actuals',views.actuals, name='actuals'),
    path('planning',views.planning, name='planning'),
    path('upload/', views.upload, name='upload'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    path('search_books/', views.search_books, name='search_books'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
