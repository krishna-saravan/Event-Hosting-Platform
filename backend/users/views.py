from rest_framework.response import Response

from .serializers import UserCreateSerializer, UserSerializer, OrganizerProfileSerializer
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView

from .models import OrganizerProfile


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data

        serializer = UserCreateSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.create(validated_data=serializer.validated_data)

        user = UserSerializer(user)
        return Response(user.data, status=status.HTTP_201_CREATED)


class RetriveUserView(APIView):

    def get(self, request):
        user = request.user

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateOrganizer(APIView):
    def post(self, request):
        user = request.user

        if user.is_organizer:
            return Response({'user already an organizer'}, status=status.HTTP_200_OK)

        user.is_organizer = True
        user.save()
        profile = OrganizerProfile.objects.create(user=user, display_name='', display_email='', display_contact='')
        profile.save()

        return Response({'organizer created'}, status=status.HTTP_200_OK)


class OrganizerProfileRetrive(APIView):

    def get(self, request):
        user = request.user

        if not user.is_organizer:
            return Response({'user is not an organizer'}, status=status.HTTP_200_OK)
        profile = OrganizerProfile.objects.get(user=user)
        serializer = OrganizerProfileSerializer(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):

        user = request.user
        try:
            profile = OrganizerProfile.objects.get(user=user)

        except:
            return Response({'unable to retrive the profile'}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data

        serializer = OrganizerProfileSerializer(profile, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'modified sucessfully'}, status=status.HTTP_201_CREATED)
        return Response({'wrong parameter'}, status=status.HTTP_400_BAD_REQUEST)
