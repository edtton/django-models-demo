from django.db import models

# Create your models here.
class Students(models.Model): 
    Gnum = models.CharField(primary_key=True, max_length=4)
    lastName = models.CharField(max_length = 20)
    firstName = models.CharField(max_length = 20)

    def __str__ (self):
        return f"G{self.Gnum}: {self.firstName} {self.lastName}"
    
class Classes(models.Model):
    CRN = models.CharField(primary_key = True, max_length = 3)
    courseID = models.CharField(max_length=6)
    courseName = models.CharField(max_length=50)

    def __str__ (self): 
        return f"CRN {self.CRN}: {self.courseID} {self.courseName}"

class Enrolled(models.Model):
    student = models.ForeignKey(Students, on_delete = models.CASCADE) 
    course = models.ForeignKey(Classes, on_delete = models.CASCADE)

    def __str__ (self): 
        return f"G{self.student.Gnum} is in {self.course.courseID}"

     