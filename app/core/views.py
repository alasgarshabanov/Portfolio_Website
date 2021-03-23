from django.shortcuts import render

from django.views.generic import TemplateView, FormView, ListView
# Create your views here.

from core.forms import ContactForm
from core.models import ContactModel, Article, Project, Service, Skill, AdminModel 


class BlogPageView(TemplateView):
    template_name = "blog-single.html"


class ContactUsView(FormView):
    form_class = ContactForm
    success_url = "/"
    template_name = "index.html"

    def form_valid(self, form):
        ContactModel.objects.create(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'),
            subject=form.cleaned_data.get('subject'),
            message=form.data.get('message'),)
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['projects'] = Project.objects.all()
        context['services'] = Service.objects.all()
        context['articles'] = Article.objects.all()
        context['admines'] = AdminModel.objects.all()
        context['skills'] = Skill.objects.all()

        project = Project.objects.all()
        service = Service.objects.all()
        article = Article.objects.all()
        admin = AdminModel.objects.all()
        skill = Skill.objects.all()

        return context
