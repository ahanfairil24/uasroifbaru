from django.urls import path

from .views import mamaviews

app_name = 'mama'
urlpatterns = [
    path('list/', mamaviews, name='mamaList')
]
