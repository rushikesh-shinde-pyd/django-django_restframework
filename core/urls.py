from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'core'

urlpatterns = [
    # path('', views.home_view, name="home"),
    path('employee/', views.EmployeeList.as_view(), name='api-list'),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view(), name='api-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
