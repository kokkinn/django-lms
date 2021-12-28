from django.urls import path

from .views import delete_group, get_groups, group_create, update_group

app_name = 'groups'
urlpatterns = [
    path('', get_groups, name='list'),
    path('create/', group_create, name="create"),
    path('update/<int:pk>/', update_group, name="update"),
    path('delete/<int:pk>/', delete_group, name="delete"),


]
