from django.db import models


class Service(models.Model):
    featured_image = models.CharField(verbose_name="Icon options: 1)ion-monitor 2)ion-code-working 3)ion-camera 4)ion-android-phone-portrait", max_length=50)
    title = models.CharField(max_length=280, verbose_name="Title")
    body = models.TextField(verbose_name="Body")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title
