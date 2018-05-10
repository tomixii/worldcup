from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addedGame/$', views.added_game, name='addedGame'),
]