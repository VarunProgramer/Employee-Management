from django.contrib import admin
from firsttry.models import empdetails

# Register your models here.

class empadmin(admin.ModelAdmin):
    emp_list = ['CodeNo', 'Name', 'Age', 'Salary', 'Address', 'Work']

admin.site.register(empdetails, empadmin)
