from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=255, unique=True, blank=True)
    url = models.CharField(max_length=255, unique=True, blank=True)
    order = models.PositiveIntegerField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.name
