from django import forms

class Homework_form(forms.Form):
    title = forms.CharField()
    subject = forms.CharField()
    final_date = forms.DateField()

class Appointment_form(forms.Form):
    title = forms.CharField()
    date = forms.DateField()
    place = forms.CharField()

class Meeting_form(forms.Form):
    title = forms.CharField()
    date = forms.DateField()
    link = forms.URLField()
    platform = forms.CharField()
