from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF' ,'Draft'
        PUBLISHED = 'PB', 'Published'

    #This is the information that stored in the tables by the makemigrations instruction
    title = models.CharField(max_length= 250) #the numbet of charachters
    slug = models.SlugField(max_length= 250)

    #This is a many to one relationship between Post class and Buildin User class
    #on_delete 'CASCADE' means that if we delet the user delete all the posts that belong
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog1_posts')
    body = models.TextField() #i can not putting the number of charachters
    publish = models.DateTimeField(default= timezone.now)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)
    status = models.CharField(max_length= 2 , choices= Status.choices, default= Status.DRAFT)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields= ['-publish']),
        ]

    #This function used to display on dashboard
    def __str__(self):
        return self.title
    



