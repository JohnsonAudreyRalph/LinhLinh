# Generated by Django 4.2.2 on 2023-12-04 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student_Management', '0016_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='job_image')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('create_at', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
