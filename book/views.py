from django.shortcuts import redirect
from .models import Contact
from .forms import ContactForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView


class ContactView(ListView):
    model = Contact
    template_name = '#'
    context_object_name = 'contact_list.html'
    ordering = ['family_name']

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact_detail.html'
    context_object_name = 'contact'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_edit.html'

    