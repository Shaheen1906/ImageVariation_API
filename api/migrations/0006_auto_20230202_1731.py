# Generated by Django 3.2.13 on 2023-02-02 12:01

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_alter_imagev_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.models.upload_to)),
                ('thumbnail', models.CharField(blank=True, max_length=255)),
                ('medium', models.CharField(blank=True, max_length=255)),
                ('large', models.CharField(blank=True, max_length=255)),
                ('grayscale', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ImageV',
        ),
    ]
