from django.contrib import admin
from .models import Student, K56DVT, Student_K56, Student_K57, Email_Class, Model_Post, new_act, Model_File, Video, new_job

# Register your models here.
@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender')
@admin.register(Student_K56)
class K56Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender')
@admin.register(Student_K57)
class K56Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender')
@admin.register(K56DVT)
class S_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender')
@admin.register(Email_Class)
class Email_Admin(admin.ModelAdmin):
    list_display = ('id', 'Name_User', 'Email_User', 'Create_User' )
@admin.register(Model_Post)
class Post_Admin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title')
@admin.register(new_job)
class job_Admin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title')
@admin.register(Model_File)
class Post_Admin(admin.ModelAdmin):
    list_display = ('id', 'name_author', 'name')
@admin.register(new_act)
class New_Admin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title')
@admin.register(Video)
class Video_Admin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title')