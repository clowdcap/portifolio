from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    autor = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200, 
                            unique=True),
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()
    data_pub = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-titulo']
    
    def __str__(self):
        return self.titulo
    
    
