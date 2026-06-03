from django.db import models
from apps.races.models import Race


class Video(models.Model):

    VIDEO_TYPE_CHOICES = [
        ("QUALIFYING_PREDICTIONS", "Qualifying Predictions"),
        ("QUALIFYING_RESULTS", "Qualifying Results"),
        ("OTHER_VIDEOS", "Other Videos")
        ("SHORTS", "Race Review"),
    ]

    title = models.CharField(
        max_length=200
    )

    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE
    )

    video_type = models.CharField(
        max_length=50,
        choices=VIDEO_TYPE_CHOICES
    )

    thumbnail = models.ImageField(
        upload_to="thumbnails/",
        blank=True,
        null=True
    )

    upload_date = models.DateField()

    views = models.IntegerField(
        default=0
    )

    ctr = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    watch_time_hours = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title