from django.shortcuts import render, redirect
from .models import Student

# Show All Data
def student_list(request):
    data = Student.objects.all()
    return render(request, 'home.html', {'data': data})

# Insert Data
def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            std_name=request.POST['name'],
            std_roll=request.POST['roll'],
            std_image=request.FILES['image'],
            std_email=request.POST['email'],
            std_city=request.POST['city']
        )
        return redirect('student_list')
    return render(request, 'add.html')

##In This Functionn We have to firstly check the method is POST or not, 
# if it is POST then we will create a new student object with the data 
#
#             std_name=request.POST['name'],
#             std_roll=request.POST['roll'],
#             std_image=request.FILES['image'],
#             std_email=request.POST['email'],
#             std_city=request.POST['city']
#std_name is the column name in the Student model and request.POST['name'] 
# is the name attribute of add student form simillarly image email and city


# # Delete Data
# def delete_student(request, id):
#     data = Student.objects.get(id=id)
#     data.delete()
#     return redirect('student_list')

# # Update Data
# def edit_student(request, id):
#     data = Student.objects.get(id=id)

#     if request.method == 'POST':
#         data.std_name = request.POST['name']
#         data.std_roll = request.POST['roll']
#         data.std_email = request.POST['email']
#         data.std_city = request.POST['city']

#         if request.FILES.get('image'):
#             data.std_image = request.FILES['image']

#         data.save()
#         return redirect('/')

#     return render(request, 'edit.html', {'data': data})