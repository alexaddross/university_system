from django.urls import path

from user.views import GetAllStudentsView

urlpatterns = [
    path('api/v1.0/users/get_all_students', GetAllStudentsView.as_view())
]