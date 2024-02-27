from django.contrib import admin
from .models import Students, Classes, Enrolled

# Register your models here.
admin.site.register(Students)
admin.site.register(Classes)
admin.site.register(Enrolled) 