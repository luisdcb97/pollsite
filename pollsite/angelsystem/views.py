from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe
from .models import User
from .scripts.treegenerator import generate_tree


class IndexView(generic.ListView):
    template_name = 'angelsystem/index.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        """Return the last five published questions."""
        return User.objects.all()


def tree(request):
    users = User.objects.all()
    json = generate_tree(users)
    context = {
        "json": mark_safe(json)
    }
    return render(request, "angelsystem/tree.html", context)
