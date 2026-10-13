from django.db import models
from django.utils import timezone


class Item(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    contact_info = models.CharField(max_length=100)
    date = models.DateField(default=timezone.localdate)

    class Meta:
        ordering = ['-date', '-id']

    def __str__(self):
        return f'{self.get_status_display()}: {self.title}'