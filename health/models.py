from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# # Profile model to extend the User model
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     age = models.IntegerField(null=True, blank=True)
#     preferences = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.user.username}'s Profile"

# from django.db import models

class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)  # Auto-increment ID
    name = models.CharField(max_length=255)  # User's name
    email = models.EmailField(unique=True)  # User's email
    date_of_birth = models.DateField(null=True, blank=True)  # Optional date of birth
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-filled timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Auto-updated timestamp

    def __str__(self):
        return self.name
