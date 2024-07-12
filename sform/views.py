from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, StudentForm, LocationForm, CollegeForm, BankForm
from .models import Student, Location, College, Bank
import random,os,string
from django.conf import settings
import requests
from django.http import JsonResponse

def fetch_bank_details(request):
    ifsc_code = request.GET.get('ifsc', '')
    if ifsc_code:
        response = requests.get(f"https://ifsc.razorpay.com/{ifsc_code}")
        if response.status_code == 200:
            return JsonResponse(response.json())
    return JsonResponse({'error': 'Invalid IFSC code or details not found'}, status=400)

def welcome_page(request):
    return render(request, 'welcome_page.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            s_code = form.cleaned_data['s_code']
            password = form.cleaned_data['password']
            user = authenticate(request, s_code=s_code, password=password)
            if user is not None:
                login(request, user)
                request.session['s_code'] = s_code  # Store s_code in session
                return redirect('student_detail', student_id=s_code)
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def student_create_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            
            edu_year = str(form.cleaned_data['edu_year'])
            random_number = ''.join(random.choices(string.digits, k=6))
            student.s_code = int(edu_year + random_number)

            # Handle community_attach file
            community_file = request.FILES.get('community_file')
            if community_file:
                # Rename community file
                community_file.name = 'community.' + community_file.name.split('.')[-1]
                student.ca_name = community_file.name
                student.community_attach = community_file.read()

            # Handle income_attach file
            income_file = request.FILES.get('income_file')
            if income_file:
                # Rename income file
                income_file.name = 'income.' + income_file.name.split('.')[-1]
                student.ia_name = income_file.name
                student.income_attach = income_file.read()

            student.set_password(student.password)  # Ensure the password is hashed
            student.save()
            return render(request, 'student_form.html', {'form': form, 's_code': student.s_code, 'submitted': True})
            
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form, 'submitted': False})


@login_required
def student_detail_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'student_detail.html', {'student': student})

def location_create_view(request):
    student = request.user
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.s_code = student
            location.save()
            return redirect('college_create')
    else:
        form = LocationForm(initial={'s_code': student})
    return render(request, 'location_form.html', {'form': form})

@login_required
def college_create_view(request):
    student = request.user
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            college = form.save(commit=False)
            college.s_code = student
            college.save()
            return redirect('bank_create')
    else:
        form = CollegeForm(initial={'s_code': student})
    return render(request, 'college_form.html', {'form': form})

@login_required
def bank_create_view(request):
    student = request.user
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save(commit=False)
            bank.s_code = student
            bank.save()
            return redirect('student_detail', student_id=student.s_code)
    else:
        form = BankForm(initial={'s_code': student})
    return render(request, 'bank_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def full_detail_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    locations = Location.objects.filter(s_code=student)
    colleges = College.objects.filter(s_code=student)
    banks = Bank.objects.filter(s_code=student)

    return render(request, 'full_detail.html', {
        'student': student,
        'locations': locations,
        'colleges': colleges,
        'banks': banks
    })

def add_other_details_view(request):
    s_code = request.session.get('s_code')
    if not s_code:
        return redirect('login')  # Redirect to login if no s_code in session

    try:
        student = Student.objects.get(s_code=s_code)
    except Student.DoesNotExist:
        return redirect('login')  # Redirect to login if student doesn't exist

    location, college, bank = None, None, None

    if request.method == 'POST':
        location_form = LocationForm(request.POST, prefix='location')
        college_form = CollegeForm(request.POST, prefix='college')
        bank_form = BankForm(request.POST, prefix='bank')
        
        Location.objects.filter(s_code=student).delete()
        College.objects.filter(s_code=student).delete()
        Bank.objects.filter(s_code=student).delete()

        if location_form.is_valid() and college_form.is_valid() and bank_form.is_valid():
            # Delete existing Location, College, Bank objects if they exist
            

            # Save new Location, College, Bank objects
            location = location_form.save(commit=False)
            location.s_code = student
            location.save()

            college = college_form.save(commit=False)
            college.s_code = student
            college.save()

            bank = bank_form.save(commit=False)
            bank.s_code = student
            bank.save()

            return redirect('student_detail', student_id=s_code)
    else:
        try:
            location = Location.objects.get(s_code=student)
        except Location.DoesNotExist:
            pass
        try:
            college = College.objects.get(s_code=student)
        except College.DoesNotExist:
            pass
        try:
            bank = Bank.objects.get(s_code=student)
        except Bank.DoesNotExist:
            pass

        location_form = LocationForm(instance=location, prefix='location', initial={'s_code': s_code})
        college_form = CollegeForm(instance=college, prefix='college', initial={'s_code': s_code})
        bank_form = BankForm(instance=bank, prefix='bank', initial={'s_code': s_code})

    context = {
        'location_form': location_form,
        'college_form': college_form,
        'bank_form': bank_form,
        'location': location,
        'college': college,
        'bank': bank,
        'student': student,  # Pass student to the template
    }
    return render(request, 'add_other_details.html', context)


