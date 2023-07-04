from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=20, validators=[MinLengthValidator(3)],
        verbose_name="Имя пользователя", unique=True,
        error_messages={
            "unique": ("Такой пользователь уже существует"),
        },
    )

    def __str__(self):
        return self.username 
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"