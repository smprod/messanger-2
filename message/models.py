from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    message = models.TextField()
    from_who = models.ForeignKey(User, related_name="from_who", on_delete=models.CASCADE)
    to_who = models.ForeignKey(User, related_name="to_who", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.from_who) + ' | ' + str(self.to_who)
