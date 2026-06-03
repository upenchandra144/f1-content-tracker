from django.db import models


class Race(models.Model):

    season = models.IntegerField()

    race_name = models.CharField(
        max_length=100
    )

    race_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.race_name} ({self.season})"