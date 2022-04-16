from email.policy import default
from django.db import models
from django.utils import timezone


class City(models.Model):

    title = models.CharField(max_length=60)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now, verbose_name="Time created")
    updated = models.DateField(auto_now=True, verbose_name="Time updated")
    is_published = models.BooleanField(default=True)
    continent = models.ForeignKey("Continent", on_delete=models.PROTECT, related_name="cities")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "cities"
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ["-created"]


class Continent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "continents"
        verbose_name = "Continent"
        ordering = ["id"]