from django.urls import path

from acme_project.acme_project.core import views

app_name = 'core'

urlpatterns = [
    path('', views.page_not_found(), name='core'),
]
