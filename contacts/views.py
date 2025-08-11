from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm
# Create your views here.

def contact_list(request):
  contacts = Contact.objects.all()
  return render(request,'contacts/contact_list.html',{"contacts":contacts})

def contact_retrieve(request,id):
  contact = Contact.objects.get(pk=id)
  return render(request,'contacts/contact_retrieve.html',{"contact":contact})

def contact_add(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('contact_list')
  else:
    form = ContactForm()
  return render(request,'contacts/contact_add.html',{"form":form})

