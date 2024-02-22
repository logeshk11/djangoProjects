from django.db import models


# Create your models here.
class Place(models.Model):
    place = models.CharField(max_length=30)
    def __str__(self):
        return self.place
class Course(models.Model):
    course = models.CharField(max_length=30)
    def __str__(self):
        return self.course


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
