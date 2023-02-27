from django.urls import path

from . import views

app_name = "news"
urlpatterns = [
    path('', views.index, name="index"),
    path('news/<int:news_id>', views.view, name="view")
]