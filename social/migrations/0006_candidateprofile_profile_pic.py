# Generated by Django 2.2.7 on 2019-12-09 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20191209_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
