from django.urls import path
from .views import EventsCreateView, EventFeed, EventDetatilView, EventRegisterView

urlpatterns = [
    path('create', EventsCreateView.as_view()),
    path('feed', EventFeed.as_view()),
    path('<str:pk>',EventDetatilView.as_view()),
    path('<str:pk>/register', EventRegisterView.as_view()),
]