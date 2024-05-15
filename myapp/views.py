from django.shortcuts import render,redirect
from .models import Students
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def homepage(request):
     # if request.method == 'POST':
     #      name = request.POST.get('name')
     #      id = request.POST.get('pass')
     #      try:
     #        student = Students.objects.get(name=name, id=id)
     #      except Students.DoesNotExist:
     #        student = None
     #      if student is not None:
     #           return render(request, "main_page.html", {})
     #      else:
     #           return render(request, "login.html", {'error_message': "Your name or your ID doesn't match any team member"})
     return render(request, "main_page.html")   
def studentmark(request):
     data=Students.objects.all()
     print(data)
     new_dict={'student_data':data}
     return render(request, "student_make_gpa.html",new_dict)
def login(request):
#     response = HttpResponse(render(request, "login.html"))
#     response['Cache-Control'] = 'no-store, no-cache, must-revalidate'
    if request.method == 'POST':
        name = request.POST.get('name')
        id = request.POST.get('pass')
        try:
            student = Students.objects.get(name=name, id=id)
        except Students.DoesNotExist:
            student = None
        if student is not None:
            return redirect(reverse('home'))
        else:
            return render(request, "login.html", {'error_message': "Your name or your ID doesn't match any team member"})
    return render(request, "login.html")
def rem(request):
          id= request.POST.get("student_Id")
          try:
            student = Students.objects.filter(id=id)
            student.delete()
          except Students.DoesNotExist:
             student= None
          if student is not None:
               return render(request, "addrem.html", {}) 
          else:
               return render(request, "addrem.html", {'error_message': "this ID doesn't match any team member"})
def add(request):
          name = request.POST.get('name')
          
          age=request.POST.get("age")
          cgpa=request.POST.get("cgpa")
          age=int(age)
          cgpa=float(cgpa)
          
          if cgpa > 4:
            return render(request, "addrem.html", {'error_message': "CGPA is out of range."})

          if age >= 100:
            return render(request, "addrem.html", {'error_message': "Age is out of range."})
          student = Students.objects.create(name=name, age=age, cgpa=cgpa)
          return render(request, "addrem.html", {}) 

def add_rem_page(request):
    return render(request, 'addrem.html')
     
          