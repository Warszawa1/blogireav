# Generated by Django 5.1 on 2024-09-26 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_image_name_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
    ]
