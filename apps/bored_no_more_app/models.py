from __future__ import unicode_literals
from django.db import models
import datetime as dt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['firstname']) < 3:
            errors["firstname"] = "First name should be longer than 2 characters!"
            print "There is an error"
        if len(postData['username']) < 3:
            errors["username"] = "First name should be longer than 2 characters!"
            print "There is an error"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email does not match the correct format"
            print "There is an error"
        if len(postData['password']) < 8:
            errors["password"] = "Password must be 8 characters"
            print "There is an error"
        if (postData['confirmation'] != postData['password']):
            errors["confirmation"] = "Passwords do not match"
            print "There is an error"
        return errors



class User(models.Model):
    firstname = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

# Create your models here.
