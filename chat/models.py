from random import randint
from django.db import models
from django.contrib.auth.models import User


# Testing Chatroom Model - EDI 92855
class ChatRoom(models.Model):
    id = models.BigAutoField(primary_key=True)

    # Creates random 5-6 character unique ID
    def save(self, *args, **kwargs):
        if not self.id:
            unique = False
            while not unique:
                eid = randint(10000, 100000)
                unique = (ChatRoom.object.filter(id=eid).count() == 0)
            self.id = eid
        super(ChatRoom, self).save(*args, **kwargs)

    object = models.Manager()

    def __str__(self):
        return "Chatroom %s" % self.id


class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(db_index=True, auto_now=True)
    text = models.TextField()
    object = models.Manager()

    def to_dict(self):
        data = {}
        data['id'] = self.id
        data['user'] = self.user
        data['time'] = self.date
        data['message'] = self.text
        return data
