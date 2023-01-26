from django.db import models

# Create your models here.


from django.db import models

from django.contrib.auth.models import (
    AbstractUser,
    UserManager as BaseUserManager,
)
# Create your models here.

class UserManger(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email: 
            raise ValueError('You must enter an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = models.CharField(max_length=255, unique=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    
    objects = UserManger()
    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']
    