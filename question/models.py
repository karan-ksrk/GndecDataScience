from django.conf import  settings
from django.db import models
from taggit.managers import TaggableManager

User = settings.AUTH_USER_MODEL

choices = (
("option1", 'option1' ),
("option2", 'option2' ),
("option3", 'option3' ),
("option4", 'option4' ),
)
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.TextField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct = models.CharField(max_length=100, choices=choices, default='option1')
    timestamp = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    def __str__(self):
        return self.question
    
