from django.urls import path
from users.views.create_profile import create_user_api
from users.views.crud_profile_api import crud_user_api
from users.views.search_api import search_view

urlpatterns = [
    path("create_profile", create_user_api),
    path("crud_profile/<int:pk>", crud_user_api),
    path("search_view", search_view),
]
