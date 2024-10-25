from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bonus_home, name='bonus_home'),
    path('client', views.client_home, name='client_home'),
    path('create', views.create, name='create'),
    path('create_card', views.create_card, name='create_card'),
    path('client/<int:pk>', views.ClientDetailView.as_view(), name='client-detail'),
    path('client/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client-delete'),
    path('<int:pk>', views.CardDetailView.as_view(), name='card-detail'),
    path('<int:pk>/update/', views.CardUpdateView.as_view(), name='card-update'),
    path('<int:pk>/delete/', views.CardDeleteView.as_view(), name='card-delete'),

]
