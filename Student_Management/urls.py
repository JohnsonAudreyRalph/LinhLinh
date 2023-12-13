from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('Post/', Post, name='Post'),
    path('creat_post/', creat_post, name='creat_post'),
    path('K55DVT/', K55DVT, name='K55DVT'),
    path('K56DVT/', K56DVTT, name='K56DVT'),
    path('Delete_s/<int:id>/', Delete_s, name='Delete_s'),
    path('Delete_56/<int:id>/', Delete_56, name='Delete_56'),
    path('Delete_post/<int:id>/', Delete_post, name='Delete_post'),
    path('Update/<str:id>', Update, name='Update'),
    path('Update_56/<str:id>', Update_56, name='Update_56'),
    # path('create_info/', create_info, name='create_info'),
    path('contact/', contact, name='contact'),
    path('new/', new, name='new'),
    path('job/', job, name='job'),
    path('environment/', environment, name='environment'),
    path('tree/', tree, name='tree'),
    path('enroll/', enroll, name='enroll'),
    path('tech/', tech, name='tech'),
    path('login', Login.as_view(), name='login'),
    path('logout/', Logout, name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('object/', object.as_view(), name='object'),
    path('document/', document.as_view(), name='document'),
    path('Delete_doc/<int:id>/', Delete_doc, name='Delete_doc'),
    path('download_document/<int:pk>/', download_document.as_view(), name='download_document'), 
    path('hocbong/', hocbong, name='hocbong'),
]