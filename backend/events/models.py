from django.db import models

from users.models import UserAccount


class Event(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False)
    venue = models.CharField(max_length=55, null=False)
    date = models.DateTimeField(null=False)
    created_At = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(UserAccount, null=False, on_delete=models.DO_NOTHING)

    def __str(self):
        return self.name


class Registration(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    Registered_At = models.DateTimeField(auto_now_add=True)
