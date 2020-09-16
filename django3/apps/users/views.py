from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views import View
from .models import UsersModel
from django.contrib.auth import login, logout,authenticate

app_name = 'users'
# Create your views here.
class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        user_grade = request.POST.get('user_grade')
        user_code = request.POST.get('user_code')
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')
        user_phone = request.POST.get('user_phone')
        user_addr = request.POST.get('user_addr')
        user = UsersModel.objects.create_user(username=user_name,password=user_password,phone=user_phone)
        user.is_active=1
        user.save()
        return render(request,'index.html')

def do_login(request):
    user_name = request.POST.get('user_name')
    user_password = request.POST.get('user_password')
    print(user_password,user_name)
    user = authenticate(username=user_name,password=user_password)
    if user is not None:
        login(request,user)
        print(request.user)
        print(request.user.username) # user.username 返回用户名
        print(request.user.password) # 获取其他属性
        # print(request.user.roleid)  # 获取其他属性
        return redirect(reverse('books:list'))
    else:
        return HttpResponse('用户名或者密码错误')

def index(request):
    return render(request,'index.html')

def do_logout(request):
    logout(request)
    return render(request,'index.html')

def update_pwd(request):
    user = request.user
    l_user = UsersModel.objects.get(id=user.id)
