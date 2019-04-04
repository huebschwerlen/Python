from django.urls import path

from .views import create_student, update_student, delete_student
from . import views


#app_name = 'WeatherApp'
urlpatterns = [
# #   path('', views.index, name='index'),
#     path('', views.IndexView.as_view(), name='index'),
#
# #   path('<int:student_id>/', views.detail, name='detail'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # path('', views.list_students, name='list_students'),
    path('', views.IndexView.as_view(), name='list_students'),

    path('new', views.create_student, name='create_students'),

    path('update/<int:id>/', update_student, name='update_student'),

    path('delete/<int:id>/', delete_student, name='delete_student'),

    # path('alerts/<int:id>/', alert_view, name='alert_view'),

    path("results/<int:student_id>/", views.alerts, name='alerts'),
]


