from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import DeviceForm

# Create your views here.

@login_required
def home(request):
  context={
    "pageTitle": "Home",
  }
  return render(request, 'home.html', context)


@login_required
def userpage(request):
  # context={
  #   'form': DeviceForm,
  #   "pageTitle": "User Page",
  # }
  # return render(request, 'userpage.html', context)

  if request.method == "POST":
    form = DeviceForm(request.POST)
    if form.is_valid():
      form.save()
    else:
      return render(request, 'home.html')
  
  context={
    'form': DeviceForm,
    "pageTitle": "User Page",
  }
  return render(request, 'userpage.html', context)


@login_required
def setting(request):
  context={
    "pageTitle": "Setting",
  }
  return render(request, 'setting.html', context)