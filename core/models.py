from django.db import models


class TimeStampedModel:

    """Time Stamped Model"""

    created = models.TimeField()
    updated = models.TimeField()

    class Meta:
        abstract = True
