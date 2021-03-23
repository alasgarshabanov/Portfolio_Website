from django.db import models
from django.utils import timezone

from .category import Category


class Project(models.Model):
    title = models.CharField(max_length=120, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    uploaded_at = models.DateTimeField()
    image = models.ImageField(null=True, verbose_name="Image")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title
