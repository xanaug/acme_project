from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    # было path('', views.birthday, name='create'),
    path('', views.BirthdayCreateView.as_view(), name='create'),
    # было path('list/', views.birthday_list, name='list'),
    path('list/', views.BirthdayListView.as_view(), name='list'),
    # было path('<int:pk>/edit/', views.Birthday, name='edit'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    # было path('<int:pk>/delete/', views.delete_birthday, name='delete'),
    path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete'),
]
