# Generated by Django 4.2.7 on 2023-11-12 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Management', '0007_new_act'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='nameFather',
        ),
        migrations.RemoveField(
            model_name='student',
            name='nameMother',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phoneContact',
        ),
    ]