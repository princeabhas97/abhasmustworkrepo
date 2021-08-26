from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from mustworkApp import views

urlpatterns = [
path('viewer/', views.my_views2),

]

urlpatterns = format_suffix_patterns(urlpatterns)