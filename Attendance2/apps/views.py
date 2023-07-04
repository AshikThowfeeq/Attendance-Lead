
import csv

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse 
from apps.models import Students,Classroom

def attendance_view(request):
    try:
        with open('./apps/attendance.csv', 'r') as file:
            reader = csv.DictReader(file)
            attendance_data = list(reader)

        context = {
            'attendance_data': attendance_data
        }
        return render(request, 'attendance.html', context)
    except FileNotFoundError:

        return HttpResponse("CSV file not found.")
        


def import_csv_to_database(request):
    try:
        with open('./apps/attendance.csv', 'r') as file:
            reader = csv.DictReader(file)
            classroom = Classroom.objects.first()  # Get the first Classroom object
            if not classroom:
                return HttpResponse("No classroom found.")

            students_to_create = []
            for row in reader:
                student = Students(
                    classroom=classroom,
                    register_no=row['reg_no'],
                    name=row['name'],
                    attendance=row['attendance']
                )
                students_to_create.append(student)

            Students.objects.bulk_create(students_to_create)

        return redirect('attendance')
    except FileNotFoundError:
        return HttpResponse("CSV file not found.")


def update_database_from_csv(request):
    try:
        classroom = Classroom.objects.first()
        if not classroom:
            return HttpResponse("No classroom found.")

        with open('./apps/attendance.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student, created = Students.objects.get_or_create(
                    register_no=row['reg_no'],
                    defaults={
                        'classroom': classroom,
                        'name': row['name'],
                        'attendance': row['attendance']
                    }
                )
                if not created:
                    student.classroom = classroom
                    student.name = row['name']
                    student.attendance = row['attendance']
                    student.save()

        return redirect('attendance')
    except FileNotFoundError:
        return HttpResponse("CSV file not found.")



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace 'home' with the name of your home page URL
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'index.html')


def homepage(request):
    return render(request, 'dashboard.html')
