from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Club(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    website= models.URLField()
    description = models.TextField()

    def __str__(self):
     return "%s" % (self.fullname)

class Adress(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
     return "%s adress" % (self.club)

class Activity(models.Model):
    name = models.CharField(max_length=200)
    clubs = models.ManyToManyField(Club)

    def __str__(self):
     return "%s" % (self.name)

class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    activity= models.ForeignKey(Activity, on_delete=models.CASCADE)
    region= models.CharField(max_length=100)
    no_participants= models.PositiveSmallIntegerField()
    date=models.DateField()
    comments=models.TextField()


class Offer(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    club= models.ForeignKey(Club, on_delete=models.CASCADE)
    price =models.DecimalField(max_digits=8, decimal_places=2)
    comments=models.TextField()

    STATUS_CHOICES = (
    (1, 'Not answered'),
    (2, 'Accepted'),
    (3, 'Declined'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
