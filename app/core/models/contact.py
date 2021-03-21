from django.db import models
from core.models import BaseModel


class ContactModel(BaseModel):
    name = models.CharField(max_length= 50, verbose_name="name")
    email = models.EmailField(max_length=50, verbose_name="email")
    subject = models.CharField(max_length=200, verbose_name="subject")
    message = models.CharField(max_length=200, verbose_name="message")


    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        
        def __str__(self):
            return self.name