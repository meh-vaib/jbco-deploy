from django.http import HttpResponse
from django.shortcuts import render, redirect
from contact.models import contact
from django.core.mail import send_mail,mail_admins

def HomePage(request):
    if request.method=="GET":
        return render(request,"index.html")
    if request.method=="POST":
        return render(request,"index.html")

def Contact(request):
    if request.method=="GET":
        return render(request,"contact.html")
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        en=contact(name=name,subject=subject,email=email,message=message)
        en.save()
        msg=name + "\n" + email + "\n" + message
        send_mail(
        subject,
        msg,
        'smithem2k22@gmail.com',
        ['mehrotravaibhav09@gmail.com'],
        fail_silently=False,
        )
        
        return render(request,"contact.html")
    
def About(request):
    return render(request,"about.html")

def Team(request):
    return render(request,"team.html")