from django.contrib import admin

from modelapp.models import Student, Course, Place

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Place)