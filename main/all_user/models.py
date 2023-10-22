from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver

class Myuser_manager(BaseUserManager):
    def _create_user(self,email,password,**extra_field):
        if not email:
            raise ValueError('Email is not valid') 
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password,**extra_field):
        extra_field.setdefault('is_staff',True)
        extra_field.setdefault('is_superuser',True)
        extra_field.setdefault('is_active',True)

        if extra_field.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_field.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True')
        if extra_field.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email,password,**extra_field)
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    premium=models.BooleanField(default=False)
    is_staff = models.BooleanField(
        gettext_lazy('staff status'),
        default=False,
        help_text = gettext_lazy('Designates whether the user can log in this site')
    )

    is_active = models.BooleanField(
        gettext_lazy('active'),
        default=True,
        help_text=gettext_lazy('Designates whether this user should be treated as active. Unselect this instead of deleting accounts')
    )

    USERNAME_FIELD = 'email'
    objects = Myuser_manager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    name=models.CharField(max_length=50,blank=True,null=True)
    addess=models.TextField(max_length=200,blank=True,null=True)
    pro_pic=models.ImageField(upload_to='pro_pic/',default='pro.png',blank=True,null=True)
    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save,sender= User)
def save_profile(sender, instance, **kwargs):
    instance.user_profile.save()