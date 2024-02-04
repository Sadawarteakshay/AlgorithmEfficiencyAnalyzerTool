# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.initiate)
# ]

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_algorithm, name='analyze_algorithm'),
    # Add other URL patterns as needed
]
