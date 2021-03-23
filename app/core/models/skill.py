from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=20, verbose_name="Name")
    percentage = models.IntegerField(verbose_name="Percentage")

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name
