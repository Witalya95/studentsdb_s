from django.contrib import admin
from students.models import Student, Group, Exam, Journal


# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Exam)
admin.site.register(Journal)
