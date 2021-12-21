"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# import debug_toolbar

from django.urls import path, include

from core.views import index
from groups.views import get_groups, group_create, update_group

from students.views import create_student, get_students, update_student, delete_student

from teachers.views import create_teacher, get_teachers, update_teacher

urlpatterns = [
    path('', index),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('groups/', include('groups.urls')),


    path('groups/', get_groups),
    path('groups/create/', group_create),
    path('groups/update/<int:pk>/', update_group, name="update_group"),
    path('teachers/', get_teachers),
    path('teachers/create/', create_teacher, name="create_teacher"),
    path('teachers/update/<int:pk>/', update_teacher, name="update_teacher"),
    # path('__debug__/', include(debug_toolbar.urls))
]
