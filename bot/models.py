from django.db import models

class botModel(models.Model):
    # TELEGRAM_TOKEN = models.CharField(max_length=255)
    user_id = models.IntegerField()
    message_id = models.IntegerField()
    # first_name
    # last_name
    # username
    # is_bot
    # sender_chat
    # vcard
    # phone_number
    # longitude
    # latitude float
    # location location
    # new_chat_members Array
    text = models.CharField(max_length=255)
