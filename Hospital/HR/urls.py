from django.urls import path

from . import views

app_name = 'HR'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:empleado_id>/', views.detail, name='detail'),
    path('<int:empleado_id>/results/', views.results, name='results'),
    path('<int:empleado_id>/vote/', views.vote, name='vote'),
]