from django.urls import path
from . import views
urlpatterns = [
    path('t1', views.home),
    path('article/<id_article>', views.view_article),
    path('articles/<int:year>/<int:month>', views.list_articles),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
]