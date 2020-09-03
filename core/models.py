from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)

    class Meta:
        abstract = True
