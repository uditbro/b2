from django.urls import path
from . import views


app_name = 'post'


urlpatterns = [
    #path for posting documents to view online.
    path('', views.article_form, name="article_form"),
]