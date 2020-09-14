from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphan = 5
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """Room Detail Definition"""

    model = models.Room