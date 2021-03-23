from django.db import models

from .category import Category


class Article(models.Model):
    title = models.CharField(max_length=60, verbose_name="Title", unique=True)
    description = models.TextField(verbose_name="Description")
    uploaded_at = models.DateTimeField()
    image = models.ImageField(null=True, verbose_name="Image")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    author = models.CharField(max_length=50)
    author_avatar=models.ImageField(verbose_name="Author avatar")

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title
