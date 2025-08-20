from django.urls import path

from tasks.views import (
    IndexView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

app_name = "tasks"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
