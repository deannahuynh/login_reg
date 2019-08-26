from django.db import models
from django.core.validators import validate_email

class UserManager(models.Manager):
   def basic_validator(self, postData):
      errors = {}
      if len(postData['firstName']) < 2:
         errors['firstName'] = "First name must contain at least 2 characters"
      if len(postData['lastName']) < 2:
         errors['lastName'] = "Last name must contain at least 2 characters"
      if postData['firstName'].isalpha() == False or postData['lastName'].isalpha() == False:
         errors['nameAlpha'] = "Name fields can only contain letters"
      # check email format
      try: 
         validate_email(postData['email'])
      except:
         errors['email'] = "Please enter a valid email"
      if postData['email']:
         users = User.objects.all()
         for user in users:
            if postData['email'] == user.email:
               errors['emailExists'] = "Email already exists"
      if len(postData['password']) < 8:
         errors['password'] = " Password must contain at least 8 characters"
      if postData['password'] != postData['confPw']:
         errors['confirmation'] = "Passwords do not match"
      return errors


class User(models.Model):
   firstName = models.CharField(max_length = 60)
   lastName = models.CharField(max_length = 60)
   email = models.CharField(max_length = 80)
   password = models.CharField(max_length = 70)
   created_at = models.DateTimeField(auto_now_add = True)
   updated_at = models.DateTimeField(auto_now = True)
   objects = UserManager() # overriding the objects with a new instance of the manager class created

class Message(models.Model):
   content = models.TextField(null=True)
   user = models.ForeignKey(User, related_name = "messages")
   created_at = models.DateTimeField(auto_now_add = True)
   updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
   content = models.TextField(null=True)
   user = models.ForeignKey(User, related_name = "comments")
   message = models.ForeignKey(Message, related_name = "comments")
   created_at = models.DateTimeField(auto_now_add = True)
   updated_at = models.DateTimeField(auto_now = True)
