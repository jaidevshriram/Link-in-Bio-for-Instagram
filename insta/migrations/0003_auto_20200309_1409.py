# Generated by Django 3.0.4 on 2020-03-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='posts/'),
        ),
    ]
