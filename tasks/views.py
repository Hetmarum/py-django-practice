from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from tasks.models import Tag


class IndexView(TemplateView):
    template_name = "tasks/index.html"


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tags_list.html"
    context_object_name = "tag_list"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context
