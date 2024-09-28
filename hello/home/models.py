from django.db import models
from django.contrib.auth.models import User

# Extending User model with a Profile model

# Other models remain the same
class Login(models.Model):
    email = models.CharField(max_length=122)
    pas = models.CharField(max_length=122)


class QueryHistory(models.Model):
    user_email = models.CharField(max_length=122)  # Optional: To associate the history with the logged-in user
    query_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.query_text} at {self.timestamp}"


class user(User):
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], null=True, blank=True)