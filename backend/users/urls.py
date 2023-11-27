from django.urls import path
from .views import RegisterView, RetriveUserView, CreateOrganizer, OrganizerProfileRetrive

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('me', RetriveUserView.as_view()),
    path('organizer', CreateOrganizer.as_view()),
    path('profile', OrganizerProfileRetrive.as_view()),
]