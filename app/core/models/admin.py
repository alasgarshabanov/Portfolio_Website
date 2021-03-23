from django.db import models

from .skill import Skill


class AdminModel(models.Model):
    name = models.CharField(max_length=120, verbose_name="Name")
    image=models.ImageField(null=True)
    profile = models.CharField(max_length=120, verbose_name="Title")
    email = models.EmailField(max_length=60, verbose_name="Email")
    phone_number = models.CharField(max_length=15, verbose_name="Phone")
    skill = models.ManyToManyField(Skill, related_name="skill")
    about = models.TextField(verbose_name="About")
