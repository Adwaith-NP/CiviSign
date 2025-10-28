from django.urls import path
from app import views

urlpatterns = [
    path("auth_node/",views.NodeAuthView.as_view(),name="auth_node"),
]