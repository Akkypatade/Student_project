from django.shortcuts import render, redirect
from student.forms import StudentForm
from student.models import student

# Create your views here.

def stud(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=StudentForm()
    return render(request,'index.html',{'form':form})


def show(request):
    students=student.objects.all()
    return render(request,"show.html",{'student':students})



def edit(request,id):
    students=student.objects.get(id=id)
    return render(request,'edit.html',{'student':students})

def update(request,id):
    students=student.objects.get(id=id)
    form=StudentForm(request.POST, instance= students)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html',{ 'student':students })

def destroy(request,id):
    students=student.objects.get(id=id)
    students.delete()
    return redirect("/show")


