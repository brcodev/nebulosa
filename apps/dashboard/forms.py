from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from apps.web.models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ['title', 'post_title', 'slug', 'description', 'content', 'image', 'alter_image', 'category', 'week', 'week_description', 'time_read']
