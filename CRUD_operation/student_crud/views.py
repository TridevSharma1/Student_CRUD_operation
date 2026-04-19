from django.shortcuts import render, redirect
from .models import Student

# Show All Data
def home(request):
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
        return redirect('/')
    return render(request, 'add.html')


# Delete Data
def delete_student(request, id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('/')

# Update Data
def edit_student(request, id):
    data = Student.objects.get(id=id)

    if request.method == 'POST':
        data.std_name = request.POST['name']
        data.std_roll = request.POST['roll']
        data.std_email = request.POST['email']
        data.std_city = request.POST['city']

        if request.FILES.get('image'):
            data.std_image = request.FILES['image']

        data.save()
        return redirect('/')

    return render(request, 'edit.html', {'data': data})