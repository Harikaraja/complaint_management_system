from django.db import models

# Create your models here.
class Complaint_Registration_Table(models.Model):
    complainer_fname=models.CharField(max_length=30)
    complainer_lname=models.CharField(max_length=40)
    complaint_title=models.CharField(max_length=60)
    complaint_timestamp=models.DateTimeField(auto_now_add=True)
    complaint_details=models.CharField(max_length=5000)
class Complaint_Registration_Table_Student(models.Model):
    complaint_id=models.CharField(max_length=30)
    complaint_title=models.CharField(max_length=60)
    complainer_fname=models.CharField(max_length=30)
    complainer_lname=models.CharField(max_length=40)
    complainer_email=models.EmailField(max_length=254)
    #complainer_rollno=models.CharField(max_length=10,primary_key=True)
    complaint_details=models.CharField(max_length=5000)
    complaint_timestamp=models.DateTimeField(auto_now_add=True)
    complaint_proof=models.FileField(upload_to='uploads/%Y/%m/%d/')
'''class Complaint_Registration_Table_Faculty(models.Model):
    complaint_id=models.CharField(max_length=30)
    complaint_title=models.CharField(max_length=60)
    complainer_fname=models.CharField(max_length=30)
    complainer_lname=models.CharField(max_length=40)
    complainer_email=models.EmailField(max_length=254)
    complaint_details=models.CharField(max_lenght=5000)
    complaint_timestamp=models.DateTimeField(auto_now_add=True)
    complaint_proof=models.FileField(upload_to='uploads/%Y/%m/%d/')'''
'''class student_registration(models.Model):
    student_id=models.AutoField()
    contact=models.IntegerField(max_length=10)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)'''



