from django.contrib import admin

from .models import *

class OnlyRead(admin.ModelAdmin):
    readonly_fields = ("published")


# Register your models here.

admin.site.register(Post)
