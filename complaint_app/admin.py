from django.contrib import admin

# Register your models here.

from .models import Complaint_Registration_Table
from .models import Complaint_Registration_Table_Student

admin.site.register(Complaint_Registration_Table)
admin.site.register(Complaint_Registration_Table_Student)