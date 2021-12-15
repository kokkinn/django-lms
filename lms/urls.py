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

from django.urls import path

from groups.views import get_groups, group_create

from students.views import create_student, get_students

from teachers.views import create_teacher, get_teachers

urlpatterns = [
    path('students/', get_students),
    path('groups/', get_groups),
    path('groups/create/', group_create),
    path('teachers', get_teachers),
    # path('__debug__/', include(debug_toolbar.urls)),
    path('students/create/', create_student, name="create_student"),
    path('teachers/create/', create_teacher, name="create_teacher")
]
