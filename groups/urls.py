from django.urls import path

from .views import GroupDeleteView, GroupUpdateView, GroupListView, GroupCreateView

app_name = 'groups'
urlpatterns = [
    path('', GroupListView.as_view(), name='list'),
    path('create/', GroupCreateView.as_view(), name="create"),
    path('update/<int:pk>/', GroupUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', GroupDeleteView.as_view(), name="delete"),


]
