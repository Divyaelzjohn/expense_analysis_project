from django.urls import path
from .views import home, edit_expense, delete_expense

urlpatterns = [
    path("", home, name="home"),
    path("edit/<int:id>/", edit_expense, name="edit"),
    path("delete/<int:id>/", delete_expense, name="delete"),
]