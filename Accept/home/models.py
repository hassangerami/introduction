from django.db import models


class Introduction(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
