# Generated by Django 3.2.13 on 2023-02-01 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='grayscale',
            field=models.ImageField(blank=True, null=True, upload_to='images/grayscales/'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='large',
            field=models.ImageField(blank=True, null=True, upload_to='images/larges/'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='small',
            field=models.ImageField(blank=True, null=True, upload_to='images/smalls/'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/thumbnails/'),
        ),
    ]
