from django.db import models

# Create your models here.
from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=100)  
    description = models.TextField(blank=True)  
	
	#  객체를 문자열로 표현하는 메서드
    def __str__(self):
        return self.title