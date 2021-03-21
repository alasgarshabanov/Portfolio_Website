from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="name", max_length=20)
    email = forms.EmailField(label="email", max_length=60)
    subject = forms.CharField(label="subject", max_length=100)
    message = forms.CharField(label="message", max_length=300)