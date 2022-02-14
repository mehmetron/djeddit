from django.urls import path

from . import views

app_name = 'threads'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:thread_id>/', views.detail, name='detail'),
    path('<int:thread_id>/vote/', views.vote, name='vote'),
    path('<int:thread_id>/results/', views.results, name='results'),
]


