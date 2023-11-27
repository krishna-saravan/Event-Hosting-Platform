from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework import permissions
from .models import Event, Registration
from .serializers import EventSerializer
from django.contrib.auth import get_user_model



class EventsCreateView(APIView):

    def post(self, request):
        user = request.user
        if not user.is_organizer:
            return Response({'only organizers can create an event'}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data

        name = data['event_name']
        description = data['event_description']
        venue = data['event_venue']
        date = data['event_date']
        organizer = user

        event = Event.objects.create(name=name, description= description, venue = venue,date = date, organizer= organizer)
        event.save()

        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EventFeed(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):

        events = Event.objects.all().order_by('date')
        serializer = EventSerializer(events, many= True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EventDetatilView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self,request,pk):

        event = Event.objects.get(id = pk)
        serializer = EventSerializer(event)
        return Response(serializer.data,status=status.HTTP_200_OK)


class EventRegisterView(APIView):

    def post(self,request, pk):

        event = Event.objects.get(id= pk)
        user = request.user
        registration = Registration(user = user, event = event)
        registration.save()

        return Response({'registration for the event is sucessful'}, status=status.HTTP_201_CREATED)