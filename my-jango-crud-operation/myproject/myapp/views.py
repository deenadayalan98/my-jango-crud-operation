from urllib import request
from django.shortcuts import render,redirect
from myapp.forms import StudentForms
from myapp.models import Student
# Create your views here.
  
def select_view(request):
    student = Student.objects.all()
    return render(request,'index.html',{'student':student})

def create_view(request):
    form = StudentForms
    if request.method == 'POST':
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')
        
    return render(request,'create.html',{'form':form})

def delete_view(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/check')

def update_view(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForms(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/check')
    
    return render(request,'update.html',{'student':student})
        