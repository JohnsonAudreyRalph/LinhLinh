# Generated by Django 4.2.7 on 2023-11-06 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Management', '0004_alter_student_age_alter_student_birthday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_User', models.CharField(max_length=150)),
                ('Email_User', models.CharField(max_length=150)),
                ('Subject_User', models.CharField(max_length=150)),
                ('Message_User', models.TextField()),
                ('Create_User', models.DateField(auto_now=True)),
            ],
        ),
    ]