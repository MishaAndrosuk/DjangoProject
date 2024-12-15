from django.urls import path

from users import views

urlpatterns = [
    path('home/', views.home),
    path('list/', views.list),
    path('<int:user_id>/', views.detail, name='detail'),
]