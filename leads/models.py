from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



#    SOURCE_CHOICES = (
#            ("YouTube", "YouTube"),
#            ("Google", "Google"),
#            ("Newsletter", "Newsletter")
#    )


class Lead(models.Model):
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

# CASCADE: If Agent is deleted, user is deleted as well.
# SET_DEFAULT, null=True, default=.
# SET_NULL, null=True.

# The "Agent" had to be defined first, else write like ("Agent")


        

#
#
#    phoned = models.BooleanField(default=False)
#    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
#
#    profile_picture = models.ImaeField(blank=True, null=True)
#    special_files = models.FileField(blank=True, null=True)

