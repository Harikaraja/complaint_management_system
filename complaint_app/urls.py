from django.contrib import admin
from django.urls import path, include
from.import views
urlpatterns = [
    path('',views.home,name="home"),
    path('registration_page',views.registration_page,name='registration_page'),
    path('fcomplaint',views.fcomplaint,name='fcomplaint'),
    path('student_complaint',views.student_complaint,name='student_complaints'),
]
