from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.

class Home(View):
    def get(self, request):
        return render(request,'index.html')
    
    
class Dashboard(View):
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
            