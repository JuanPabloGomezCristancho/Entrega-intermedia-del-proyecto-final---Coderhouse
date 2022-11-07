from django.shortcuts import render

from blog_own.models import Homework, Appointment, Meeting
from blog_own.forms import Homework_form, Appointment_form, Meeting_form

# Create your views here.

def inicio_blog(request):
    return render(request, 'blog_own/start.html')

def homework_add(request):
    if request.method == 'POST':
        form = Homework_form(request.POST) # Llega toda la informacion del Html.
        print(form)
        if form.is_valid: # Lo valida Django
            information = form.cleaned_data
            homework = Homework( title=information['title'], subject=information['subject'], final_date=information['final_date'])
            homework.save()
            return render(request, "blog_own/start.html")

    else:
        form = Homework_form() # Formulario vacio para construir el html.
    
    return render(request, "blog_own/homework.html", {"form": form})

def appointment_add(request):
    if request.method == 'POST':
        form = Appointment_form(request.POST) # Llega toda la informacion del Html.
        print(form)
        if form.is_valid: # Lo valida Django
            information = form.cleaned_data
            appointment = Appointment(title=information['title'], place=information['place'], date=information['date'])
            appointment.save()
            return render(request, "blog_own/start.html")

    else:
        form = Appointment_form() # Formulario vacio para construir el html.
    
    return render(request, "blog_own/appointment.html", {"form": form})

def meeting_add(request):
    if request.method == 'POST':
        form = Meeting_form(request.POST) # Llega toda la informacion del Html.
        print(form)
        if form.is_valid: # Lo valida Django
            information = form.cleaned_data
            meeting = Meeting(title=information['title'], date=information['date'], link=information['link'],  platform=information['platform'])
            meeting.save()
            return render(request, "blog_own/start.html")

    else:
        form = Meeting_form() # Formulario vacio para construir el html.
    
    return render(request, "blog_own/meeting.html", {"form": form})

def search_homework(request):
    return render(request, "blog_own/search_homework.html")

def search_appointment(request):
    return render(request, "blog_own/search_appointment.html")

def search_meeting(request):
    return render(request, "blog_own/search_meeting.html")

def search_date_homework(request):
    if request.GET["date"]:
        date = request.GET["date"]
        objects = Homework.objects.filter(final_date__icontains=date) # Ojo con el platform OOOOOO.OOOOOOOO

        return render(request, "blog_own/search_results_homework.html", {"objects": objects, "date":date})
    
    else:
        answer = "No se enviaron datos"
    
    return HttpResponse(answer)

def search_date_appointment(request):
    if request.GET["date"]:
        date = request.GET["date"]
        objects = Appointment.objects.filter(date__icontains=date)

        return render(request, "blog_own/search_results_appointment.html", {"objects": objects, "date":date})
    
    else:
        answer = "No se enviaron datos"
    
    return HttpResponse(answer)

def search_date_meeting(request):
    if request.GET["date"]:
        date = request.GET["date"]
        objects = Meeting.objects.filter(date__icontains=date)

        return render(request, "blog_own/search_results_meeting.html", {"objects": objects, "date":date})
    
    else:
        answer = "No se enviaron datos"
    
    return HttpResponse(answer)