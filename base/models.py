from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=50, null=False, blank=False, default='user')
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    date_register = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(null=True, blank=True, upload_to='user-images/', default='user-images/avatar.webp')
    address = models.CharField(max_length=200, null=True, blank=True)
    phoneno = models.CharField(max_length=11, null=False, blank=False, default='xxxxxxxxxxx')
    dob = models.DateField(null=False, blank=False, default=timezone.now)    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    duedate = models.DateTimeField(null=True, blank=True)
    lastchange = models.DateTimeField(auto_now=True)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    document = models.FileField(null=True, blank=True, upload_to='documents/')
    complete = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['complete', 'duedate']
        
    def __str__(self):
        return self.title
    
    @property
    def status(self):
        if self.duedate and self.duedate < timezone.now():
            return "Incomplete"
        else:
            return "Pending"