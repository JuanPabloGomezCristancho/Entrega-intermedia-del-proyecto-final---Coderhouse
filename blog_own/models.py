from django.db import models

class Homework(models.Model):
    title = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    final_date = models.DateField()

class Appointment(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateField()
    place = models.CharField(max_length=40)
    

class Meeting(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateField()
    link = models.URLField(max_length=200)
    platform = models.CharField(max_length=20)