# Generated by Django 4.1.7 on 2023-03-19 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_profile1_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile1',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photo'),
        ),
        migrations.AddField(
            model_name='profile1',
            name='region',
            field=models.CharField(choices=[('B', 'Bishkek'), ('O', 'Osh'), ('N', 'Naryn'), ('A', 'Batken'), ('I', 'Issyk-kul'), ('D', 'Djalal-abad'), ('T', 'Talas')], default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='profile1',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
