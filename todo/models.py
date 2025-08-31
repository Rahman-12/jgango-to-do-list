from django.db import models
from django.conf import settings
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=True)  # Allow null for existing tasks
    # Default to now for existing tasks
    created_at = models.DateTimeField(default=timezone.now)
    # This will work without issues
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
