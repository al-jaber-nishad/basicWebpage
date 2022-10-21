from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import DeviceForm, NewUserForm, SearchForm

from django.contrib.auth import login
from django.contrib import messages
from .models import *

from datetime import date, datetime
import time
# Create your views here.



def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"form":form})

@login_required
def home(request):

  useremail = request.user.email

  if request.method == "POST":
    form = DeviceForm(request.POST)
    if form.is_valid():
      devicelist = form.save(commit=False)
      devicelist.username = request.user.username
      devicelist.save()
      return redirect('/')
    else:
      return render(request, 'home.html')
  
  context={
    'form': DeviceForm,
    "pageTitle": "User Page",
    'useremail': useremail, 
  }
  return render(request, 'home.html', context)


@login_required
def setting(request):

  # all_object = nordpool.
  import mysql.connector

  mydb = mysql.connector.connect(
      host="localhost",
      user="user1", 
      password="asdf",
      database="SmartplugDB"
  )

  mycursor = mydb.cursor()

  t = time.localtime()
  current_time = str(time.strftime("%H", t))

  current_region = Device.objects.filter(username=request.user.username).values()[0]['region']
  print(current_region)

  today = str(date.today())
  

  if request.method == "POST":
    form = SearchForm(request.POST)
    if form.is_valid():
      form_time = form.cleaned_data.get('time')
      time_hr = int(form_time) + int(current_time)
      print(form_time)
      time_hr = str(time_hr % 24)
      print(today, time_hr, current_time)
      print('test')
      
      sql = "SELECT MIN("+current_region+") FROM nordpool WHERE Date='"+today+"'"

      # AND ('"+time_hr+"' >= Hour AND '"+current_time+"' <= Hour) 

      mycursor.execute(sql)
      # mydb.commit()
      cursor_data = mycursor.fetchall()

      print("Minimum on today: ",cursor_data)


      
      return redirect('/setting')
    else:
      return render(request, 'home.html')
  

  

  # cheapest_hour_of_day = 
  # print(today)
  username = request.user.username
  sql = "SELECT MIN("+current_region+") FROM nordpool WHERE Date='"+today+"'"
  sql2 = "SELECT Date, Hour, "+current_region+" FROM nordpool WHERE Date='"+today+"'"

  mycursor.execute(sql)

  # mydb.commit()
  cursor_data = mycursor.fetchall()
  cheapest_val_of_day = cursor_data
  print("Cheapest val of the day", cheapest_val_of_day)
  # column_names = column_names[3:]
  mycursor.close()


  mycursor = mydb.cursor()
  mycursor.execute(sql2)
  # mydb.commit()
  cursor_data = mycursor.fetchall()
  cheapest_hour_of_day = cursor_data
  print("Cheapest hour of the day", cheapest_hour_of_day)

  
  form = SearchForm()
  context={
    "pageTitle": "Setting",
    'cheapest_val_of_day': cheapest_val_of_day,
    'cheapest_hour_of_day': cheapest_hour_of_day,
    'form': form,

  }
  return render(request, 'setting.html', context)