from django.conf import settings
from django.db import models

class Chat_room(models.Model):
    participants = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chat_msg = models.TextField()
