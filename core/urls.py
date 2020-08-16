from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as auth_views


app_name = 'core'

urlpatterns = [
    # path('', views.home_view, name="home"),
    path('employee/', views.EmployeeList.as_view(), name='api-list'),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view(), name='api-details'),
    path('get-api-token/', auth_views.obtain_auth_token, name='get-api-token'),
    # path('api-auth/', include('rest_framework.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns)
