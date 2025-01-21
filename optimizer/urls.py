from django.urls import path
from .views import BuildRequestView

urlpatterns = [
    path('', BuildRequestView.as_view(), name='build_request'),
]
