from django.contrib import admin
from .models import ContactModel, Article, Category, Project, Service, AdminModel, Skill

admin.site.register(ContactModel)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(AdminModel)
admin.site.register(Skill)
