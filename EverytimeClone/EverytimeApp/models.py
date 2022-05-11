from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    file = models.FileField(default="")
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.title