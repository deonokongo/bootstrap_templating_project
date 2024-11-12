from django.urls import path
from . import views

app_name = 'templating_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('specials/', views.specials, name='specials'),
    path('events/', views.events, name='events'),
    path('chefs/', views.chefs, name='chefs'),
    path('gallery/', views.gallery, name='gallery'),
    path('book-a-table/',views.book_a_table, name='book_table'),
]