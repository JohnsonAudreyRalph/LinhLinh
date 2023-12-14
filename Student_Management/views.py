from django.shortcuts import render, redirect
from .models import Student, Email_Class, Model_Post, new_act, K56DVT, Model_File, new_job, Student_K56, Student_K57
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import format_html
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import FileResponse



# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        if request.method == "POST":
            username = request.POST.get('UserName')
            Password = request.POST.get('Password')
            user = authenticate(username=username, password=Password)
            if user is not None:
                auth_login(request, user)
                messages_ = username
                return redirect('/', {'messages':username})
                # return render(request, 'register.html')
            else:
                try:
                    # Kiểm tra điều kiện tên người dùng nhập vào có tồn tại hay không
                    User.objects.get(username=username)
                    # Nếu người dùng có tồn tại, nhưng mật khẩu sai ==> Reload lại trang web để người dùng đăng nhập lại
                    messages.error(request, "Sai thông tin đăng nhập!!!!")
                    return redirect('/login')
                except User.DoesNotExist:
                    messages.error(request, "Không tồn tại tài khoản này")
                    return redirect('/login')
                
class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        if request.method == "POST":
            Username = request.POST.get('Username')
            Email = request.POST.get('Email')
            Password = request.POST.get('Password')
            Conf_Password = request.POST.get('Conf_Password')
            if User.objects.filter(username=Username):
                messages.error(request, "Tài khoản đã tồn tại! Hãy đăng ký tài khoản khác")
                return render(request, 'register.html')
            if User.objects.filter(email=Email).exists():
                messages.error(request, "Email đã tồn tại")
                return render(request, 'register.html')
            if Password!=Conf_Password:
                messages.error(request, "Mật khẩu không khớp!")
                return render(request, 'register.html')
            MyUser = User.objects.create_user(Username, Email, Password)
            print(Username, Email, Password)
            MyUser.save()
            return redirect('/login')
        return render(request, 'register.html')
    
def Logout(request):
    logout(request)
    return redirect('/')

class object(View):
    def get(self, request):
        return render(request, 'object.html')
    def post(self, request):
        # ms=['nam1','nam_cuoi','ph','csv','khac']
        if request.method == "POST":
            obj = request.POST.getlist('obj')
            # print(obj)
            if obj==['nam1']:
                return render(request,'tree.html')
            if obj==['nam_cuoi']:
                All_job = new_job.objects.all()
                return render(request,'job.html', {'All_job':All_job})
            if obj==['ph']:
                return render(request, 'home.html')
            if obj==['csv']:
                All_Post = Model_Post.objects.all()
                return render(request, 'Post.html', {'All_Post':All_Post})
                
            if obj==['khac']:
                return render(request,'enroll.html')
        return render(request, 'object.html')
    

class Home(View):
    def get(self, request):
        return render(request, 'home.html')

class document(View):
    def get(self, request):
        Show_doc = Model_File.objects.all()
        return render(request, 'document.html', {'Doc':Show_doc})


class download_document(View):
    def get(self, request, pk):
        file_model = get_object_or_404(Model_File, pk=pk) # Dùng để lấy đối tượng Model_File từ cơ sở dữ liệu với khóa chính là pk. Nếu không tìm thấy đối tượng, nó sẽ trả về trang 404 (Page Not Found).
        file_path = file_model.file.path # Lấy đường dẫn đến tệp tin từ trường file của đối tượng Model_File. Đây là đường dẫn tuyệt đối đến tệp tin trên hệ thống tệp của máy chủ.
        response = FileResponse(open(file_path, 'rb')) # Tạo một đối tượng để trả về nội dung của tệp tin, thực hiện mở nội dung tệp tin ở chế độ đọc
        response['Content-Type'] = 'application/octet-stream' # Thiết lập nội dung phản hồi để báo trình duyệt xử lý dữ liệu tải xuống thay vì để hiển thị dữ liệu trực tiếp trên trình duyệt
        response['Content-Disposition'] = f'attachment; filename="{file_model.file.name}"' # Lấy tệp tin tải xuống, đặt tên cho tệp tin tải xuống là tên của file đó
        return response # Điều này thực hiện báo cho trình duyệt người dùng tải xuống

def Post(request):
    All_Post = Model_Post.objects.all()
    return render(request, 'Post.html', {'All_Post':All_Post})



def new(request):
    All_New = new_act.objects.all()
    return render(request, 'new.html', {'All_New': All_New} )

def job(request):
    All_job = new_job.objects.all()
    return render(request, 'job.html', {'All_job': All_job} )


def tree(request):
    return render(request, 'tree.html')
def teacher(request):
    return render(request, 'teacher.html')

def hocbong(request):
    return render(request, 'hocbong.html')
def environment(request):
    return render(request, 'environment.html')

def K56DVTT(request):
    ds = Student_K56.objects.all()
    return render(request, 'K56DVT.html', {'ds':ds})

def K55DVT(request):
    students = Student.objects.all()
    return render(request, 'K55DVT.html', {'students': students})

def creat_post(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.user
        if image and title and description and author:
            s = Model_Post(image=image, title=title, description=description, author=author)
            s.save()
        return redirect('/Post/')
    return render(request, 'creat_post.html')

def Delete_s(request, id):
    if request.method == 'POST':
        id_delete = Student.objects.get(pk=id)
        id_delete.delete()
        return redirect('K55DVT')
def Delete_56(request, id):
    if request.method == 'POST':
        id_delete = Student_K56.objects.get(pk=id)
        id_delete.delete()
        return redirect('K56DVT')
def Delete_doc(request, id):
    if request.method == 'POST':
        id_delete = Model_File.objects.get(pk=id)
        id_delete.delete()
        return redirect('document')
def Delete_post(request, id):
    if request.method == 'POST':
        i_delete = Model_Post.objects.get(pk=id)
        i_delete.delete()
        return redirect('Post')

def Update(request, id):
    if request.method == "POST":
        edit_name = request.POST.get('edit_name')
        edit_image = request.FILES.get('edit_image')
        edit_gender = request.POST.get('edit_gender')
        edit_study = request.POST.get('edit_study')
        edit_act = request.POST.get('edit_act')
        author = request.user
        if edit_name and edit_image and edit_gender and edit_study and edit_act and author:
            save = Student(id=id, name=edit_name, author=author, image=edit_image, gender=edit_gender, study=edit_study, act=edit_act)
            save.save()
            return redirect('K55DVT')
        students = Student.objects.all()
    return render(request, 'K55DVT.html', {'students':students})
def Update_56(request, id):
    if request.method == "POST":
        edit_name = request.POST.get('edit_name')
        edit_image = request.FILES.get('edit_image')
        edit_gender = request.POST.get('edit_gender')
        edit_study = request.POST.get('edit_study')
        edit_act = request.POST.get('edit_act')
        author = request.user
        if edit_name and edit_image and edit_gender and edit_study and edit_act and author:
            save_56 = Student_K56(id=id, name=edit_name, image=edit_image, author=author, gender=edit_gender, study=edit_study, act=edit_act)
            save_56.save()
            return redirect('K56DVT')
        ds = Student_K56.objects.all()
    return render(request, 'K56DVT.html', {'ds':ds})

def contact(request):
    
    # Subject = "Đây là subject trang liên hệ "
    # Message = "Đây là mesage gửi từ admin sang user"
    # From_Email = settings.EMAIL_HOST_USER
    # To_Email = ['K195520207036@tnut.edu.vn']
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Subject = request.POST.get('subject')
        Message = request.POST.get('message')
        
        Subject = Subject
        Message = Message
        From_Email = settings.EMAIL_HOST_USER
        To_Email = Email
        
        Subject_Response  = 'Thư phản hồi'
        Message_Response = format_html(f'Xin cảm ơn bạn <b> {Name} </b>. <p>Yêu cầu của bạn đang được chúng tôi xem xét.</p> <p>Chúc bạn một ngày vui vẻ.</p> ')
        print(f'Name: {Name}, Email: {Email}, Subject: {Subject}, Message: {Message}')
        send_mail(
            Subject_Response,
            Message_Response,
            From_Email,
            [To_Email],
            fail_silently=False,
            html_message=Message_Response
        ) 
        
        save = Email_Class(Name_User=Name, Email_User=Email, Subject_User=Subject, Message_User=Message)
        save.save()
    return render(request, 'contact.html')



def login(request):
    return render(request, 'login.html')
def tech(request):
    return render(request, 'tech.html')
def enroll(request):
    return render(request, 'enroll.html')