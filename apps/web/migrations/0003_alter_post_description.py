# Generated by Django 4.2.5 on 2023-10-06 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_post_week_post_week_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, max_length=700, null=True),
        ),
    ]
