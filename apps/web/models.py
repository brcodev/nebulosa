from apps.category.models import Category
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from core.settings import AUTH_USER_MODEL
from django.db.models.signals import pre_save
from django.dispatch import receiver
User = AUTH_USER_MODEL




# Create your models here.

class Post(models.Model):
    
    id =            models.AutoField(primary_key=True)
    title =         models.CharField(max_length=120, null=False)
    post_title =    models.CharField(max_length=255, null=False)
    slug =          models.SlugField(max_length=255, unique=True)
    author =        models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    description =   models.TextField(max_length=700, blank=True, null=True) 
    content =       RichTextUploadingField(blank=True, null=True)
    image =         models.ImageField(upload_to='images/posts/', max_length=500, blank=False, null=False)
    alter_image =   models.ImageField(upload_to='images/posts/', max_length=500, blank=True, null=True)
    
    category =      models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    time_read =     models.IntegerField(blank=True, null=True)
    published =     models.DateTimeField(default=timezone.now)
    
    week = models.BooleanField(default=False)
    week_description = models.TextField(max_length=2000, blank=True, null=True) 
    
    def __str__(self):
        return self.title
    
        
    def delete(self, using=None, keep_parents=False) :
        self.image.storage.delete(self.image.name)
        return super().delete()
    
    
@receiver(pre_save, sender=Post)
def week_post(sender, instance, **kwargs):
    if instance.week:
        # Si este post se marca como 'week', desmarcar todos los demás.
        sender.objects.exclude(pk=instance.pk).update(week=False)
    
    
    
    
