from django.urls import path
from blog_own import views

urlpatterns = [
    path('', views.inicio_blog, name='start_blog'),
    path('homework', views.homework_add, name='homework_add'),
    path('appointment', views.appointment_add, name='appointment_add'),
    path('meeting', views.meeting_add, name='meeting_add'),

    path('search_homework', views.search_homework, name="search_homework"),
    path('search_apponintmnet', views.search_appointment, name="search_appointment"),
    path('search_meeting', views.search_meeting, name="search_meeting"),

    path('search_results_homework', views.search_date_homework),
    path('search_results_appointment', views.search_date_appointment),
    path('search_results_meeting', views.search_date_meeting),
]