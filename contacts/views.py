from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


# list
@login_required
def contact_list(request):
  user = request.user
  query = request.GET.get('q',"")
  sort_by = request.GET.get('sort',"name")

  # cotacts_list
  # contacts = Contact.objects.all()
  contacts = Contact.objects.filter(user = user)
  # search
  if query:
    contacts = contacts.filter(
      Q(name__icontains=query) |
      Q(email__icontains=query) |
      Q(phone__icontains=query) 
    )

  # sort
  contacts = contacts.order_by(sort_by)
  # pagination
  paginator = Paginator(contacts,15)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request,'contacts/contact_list.html',{
                                                      # "query":query if query is not None else ""
                                                      "query":query,
                                                      "sort_by":sort_by,
                                                      "page_obj":page_obj,
                                                      "user":user
                                                     })

# retrieve 
@login_required
def contact_retrieve(request,id):
  contact = Contact.objects.get(pk=id ,user=request.user)

  # if contact.user.pk = request.user.id:
  
  return render(request,'contacts/contact_retrieve.html',{"contact":contact})

# add
@login_required
def contact_add(request):
  if request.method == "POST":
    form = ContactForm(request.POST,user=request.user)
    if form.is_valid():
      form.save()
      # contact= form.save(commit=False)
      # contact.user = request.user
      # contact.save()

      return redirect('contact_list')
  else:
    form = ContactForm()
  return render(request,'contacts/contact_add.html',{"form":form})


#edit
@login_required
def contact_edit(request,contact_id):
  contact = get_object_or_404(Contact,id=contact_id,user=request.user )
    # if contact.user.pk = request.user.id:
  if request.method == "POST":
    form = ContactForm(request.POST,instance=contact)
    if form.is_valid():
      form.save()
      return redirect('contact_list')
    
  else :
    form = ContactForm(instance=contact)
  return render(request,'contacts/contact_edit.html',{'form':form,'contact':contact})


# delete
@login_required
def contact_delete(request,contact_id):
  contact = get_object_or_404(Contact,id=contact_id,user=request.user  )
     # if contact.user.pk = request.user.id:
  if request.method == "POST":
   
    contact.delete()
    return redirect('contact_list')
  return render(request,'contacts/contact_delete.html',{'contact':contact})

  

