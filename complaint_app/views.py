from django.shortcuts import render
from django.http import HttpResponse

from .models import Complaints_Registration_Table
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
    obj1 = Complaints_Registration_Table.objects.all()
    return render(request,'complaint_page2.html',{"Complaint_Registration_Table":obj1})
    
    