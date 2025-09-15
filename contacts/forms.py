from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
  def __init__(self,*args,**kwargs):
    self.user = kwargs.pop('user',None)
    super().__init__(*args,**kwargs)


  class Meta:
    model = Contact
    fields = ['name','age','phone','email']
  
  def save(self, commit=True):
    contact = super().save(commit=False)
    contact.user = self.user
    if commit:
      contact.save()
    return contact
    