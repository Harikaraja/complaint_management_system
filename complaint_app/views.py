from django.shortcuts import render
from django.http import HttpResponse
from .models import Complaint_Registration_Table
# Create your views here.
def  home(request):
    return render(request,"login_page.html")
def registration_page(request):
    return render(request,'Registration_page.html')
def fcomplaint(request):
    return render(request,'Faculty_complaint_registration.html')
def student_complaint(request):
    return render(request,'Student_complaint_registration.html')
def complaint_page(request):
    obj1 = Complaint_Registration_Table.objects
    return render(request,'complaint_page2.html',{'objs':obj1})
