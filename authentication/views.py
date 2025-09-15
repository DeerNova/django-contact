from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import login,logout
# Create your views here.
def register_form(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      return redirect('contact_list')
    
  else:
    form = RegisterForm()
  return render(request,'accounts/register.html',{'form':form})


def login_form(request):
  if request.method == "POST":
    form = LoginForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request,user)
      return redirect('contact_list')
    
  else:
    form = LoginForm()
  return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
  logout(request)
  return redirect('login')