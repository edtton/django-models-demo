from django.shortcuts import render
from .models import Students, Classes, Enrolled 

# Create your views here.

def index(request):
    return render(request, "students/index.html", {
        "students": Students.objects.all()
    })

def course(request, courseID):
    course = Classes.objects.get(courseID = courseID)
    return render(request, "students/courses.html", {
        "course": course 
    })
