
# Create your views here.
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.http import request, HttpResponse
from django.shortcuts import render

from education.models import Student, Teacher, Mentor
from .forms import *
import openpyxl
# Create your views here.


def home(request):
    if request.method=='GET':
        return render(request,'home.html')


def education(request):
    if request.method == 'GET':
        return render(request, 'education.html')


def healthcare(request):
    if request.method == 'GET':
        return render(request,'healthcare.html')


def livelihood(request):
    if request.method=='GET':
        return render(request,'livelihood.html')


def about(request):
    if request.method=='GET':
        return render(request,'aboutpage.html')


def index(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(user)
            teachertemp = Teacher.objects.filter(user=user)
            if teachertemp is not None:
                return render(request, 'teacher_home.html')
            else:
                return render(request, 'mentor_home.html')
        return HttpResponse("Authentication Failed")
    else:
        form = LoginForm
        return render(request, 'login.html', {'form': form})


def UserFormView(request):

    if request.method=='GET':
        form = UserForm
        return render(request,'registrationForm.html',{'form':form})

    else:
        form = UserForm(request.POST)
        if form.is_valid():
            # make a user object of the form data, but dont put it in database yet
            user = form.save(commit=False)


            #clean the data
            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']
            print(age)
            area = form.cleaned_data['area']
            role = form.cleaned_data['role']
            #user = User()
            user.set_password(password)
            user.username = username
            user.save()
            if role=='teacher':
                teacher = Teacher(user=user,age=age,area=area)
                teacher.save()
                print('hiii')
                print(teacher)
            else :
                mentor = Mentor()
                mentor.user = user
                mentor.age = age
                mentor.area = area
                mentor.save()

            # returns user object if credentials are correct
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if role=='teacher':
                    return render(request,'teacher_home.html',{'name':'name'})
                else:
                    return render(request,'mentor_home.html')

        return render(request,'registrationForm.html', {'form': form})


def fileUpload(request):
    if "GET" == request.method:
        return render(request, 'upload_xlsx.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)
        #if excel_file.endswith('.xlsx'):
            # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        return render(request, 'upload_xlsx.html', {"excel_data":excel_data})
