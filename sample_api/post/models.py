from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Post(title={self.title}, description={self.description})'
    
