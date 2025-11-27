from django.urls import path
from . import views

urlpatterns = [
    path('add-route/', views.add_route, name='add_route'),
    path('find-nth-node/', views.find_nth_node, name='find_nth_node'),
    path('longest-route/', views.longest_route, name='longest_route'),
    path('shortest-path/', views.shortest_path, name='shortest_path'),
]