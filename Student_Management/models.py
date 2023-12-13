from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Model_Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_image', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    create_at = models.DateField(auto_now=True)


class Model_File(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='doc', null=True, default=None)
    image = models.ImageField(upload_to='file_image',null=True, blank=True)
    name = models.CharField(max_length=255)
    name_author = models.CharField(max_length=255)
    create_at = models.DateField(auto_now=True)    

class Video(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='video', null=True, default=None)
    title = models.CharField(max_length=200)

class Student(models.Model):
    Gender_choices = [
        ("Nam", "Nam"),
        ("Nữ", "Nữ"),
        ("Khác", "Khác")
    ]
    image = models.ImageField(upload_to='student_image', null=True, blank=True)
    name = RichTextField(blank=True, null=True)
    gender = models.CharField(choices=Gender_choices, max_length=10)
    study = RichTextField(blank=True, null=True)
    act = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    
class Student_K56(models.Model):
    Gender_choices = [
        ("Nam", "Nam"),
        ("Nữ", "Nữ"),
        ("Khác", "Khác")
    ]
    image = models.ImageField(upload_to='student56_image', null=True, blank=True)
    name = RichTextField(blank=True, null=True)
    gender = models.CharField(choices=Gender_choices, max_length=10)
    study = RichTextField(blank=True, null=True)
    act = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    
class Student_K57(models.Model):
    Gender_choices = [
        ("Nam", "Nam"),
        ("Nữ", "Nữ"),
        ("Khác", "Khác")
    ]
    image = models.ImageField(upload_to='student57_image', null=True, blank=True)
    name = RichTextField(blank=True, null=True)
    gender = models.CharField(choices=Gender_choices, max_length=10)
    study = RichTextField(blank=True, null=True)
    act = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")


class K56DVT(models.Model):
    Gender_choices = [
        ("Nam", "Nam"),
        ("Nữ", "Nữ"),
        ("Khác", "Khác")
    ]
    image = models.ImageField(upload_to='k56_image',null=True, blank=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=Gender_choices, max_length=10)
    classs = models.CharField(max_length=10)
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=300)
    mssv = models.CharField(max_length=30)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=50)



class Email_Class(models.Model):
    Name_User = models.CharField(max_length=150)
    Email_User = models.CharField(max_length=150)
    Subject_User = models.CharField(max_length=150)
    Message_User = models.TextField()
    Create_User = models.DateField(auto_now=True)
    
class new_act(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='new_image', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    create_at = models.DateField(auto_now=True)
    
class new_job(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='job_image', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    create_at = models.DateField(auto_now=True)    


