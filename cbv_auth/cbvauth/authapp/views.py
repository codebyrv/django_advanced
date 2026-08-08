from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from authapp.models import Student
# Create your views here.

class Home(View):
    def get(self, request):
        return render(request,'index.html')
    
    
class Dashboard(LoginRequiredMixin,View):
    def get(self, request):
        return render(request,'dashboard.html')    
    
class RegisterView(View):
    
    def get(self,request):
        return render(request,'register.html')
    
    
    def post(self,request):
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password1")
        password2=request.POST.get("password2")
        if password!=password2: 
            messages.info(request,"password not matchh")
            return render(request,'register.html')
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exists")    
            return render(request,'register.html')
        if User.objects.filter(email=email).exists():
            messages.info(request,"email exists")   
            return render(request,'register.html')
        else:
            User.objects.create_user(email=email,username=username,password=password)
        return  redirect('login')    
    
class LoginView(View):
    
    def get(self,request):
        
        return render(request,'login.html')
    
    
    def post(self, request):
        
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        
        user=authenticate(username=username,password=password)
        
        
        if user:
            
            login(request,user)
            return redirect('dashboard')
        
        else:
            
            messages.info(request,"invalid username or password, check again ")
            return render(request,'login.html')
            
from django.contrib.auth import logout
from django.views import View
from django.shortcuts import redirect


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')            
            
            
class Create(LoginRequiredMixin,View):
    
    
    
    
    def get(self,request):
        students=Student.objects.all()
        return render(request,'create.html',{"students":students})            
    
    def post(self,request):
        
        name=request.POST.get("name")
        age=request.POST.get("age")
        course=request.POST.get("course")
        
        
        Student.objects.create(name=name,age=age,course=course,created_by=request.user)
        
        messages.success(request,"SAVED")
        
        return redirect('dashboard')
    
    

class ListView(LoginRequiredMixin,View):
    
    def get(self,request):
        
        list=Student.objects.filter(created_by=request.user)
        
        return render(request,'list.html',{"list":list})
    
    
    
class UpdateView(LoginRequiredMixin, View):
    
    
    def get(self,request,id):
        
        student=get_object_or_404(Student,id=id)
        
        return render(request,'update.html')