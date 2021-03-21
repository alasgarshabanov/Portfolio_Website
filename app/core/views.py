from django.shortcuts import render

from django.views.generic import TemplateView, FormView
# Create your views here.

from core.forms import ContactForm


class HomePageView(TemplateView):
    template_name = "index.html"



class ContactUsView(FormView):
    form_class = ContactForm
    success_url = "/"
    template_name = "partials/contact.html"

    def form_valid(self, form):
        ContactModel.objects.create(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'),
            subject=form.cleaned_data.get('subject'),
            message=form.data.get('message'),)
        return super().form_valid(form)