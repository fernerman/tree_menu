from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from .models import Employer
from django.contrib.auth import logout

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import EmployerForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If user is authenticated, log in the user
            login(request, user)
            return redirect('manage_employers')
        else:
            # If authentication fails, show an error message
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def manage_employers(request):
    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('manage_employers')  # Redirect to the same page after form submission or deletion
    else:
        # If the request method is GET, display the form and employers list
        form = EmployerForm()
        employers = Employer.objects.all()
        return render(request, 'main.html', {'form': form, 'employers': employers})


@login_required(login_url='login')
def delete_employer(request, employer_id):
    # Get the record to delete
    employer = get_object_or_404(Employer, pk=employer_id)
    # Delete the record
    employer.delete()
    return redirect('manage_employers')  # Redirect to the same page after deletion


@login_required(login_url='login')
def edit_employer(request, employer_edit_id):
    # Get the record to edit
    employer = get_object_or_404(Employer, pk=employer_edit_id)
    form = EmployerForm(instance=employer)
    if request.method == 'POST':
        form = EmployerForm(request.POST, instance=employer)
        if form.is_valid():
            form.save()
            return redirect('manage_employers')  # Redirect to the list of records after editing

    return render(request, 'main.html', {'form': form})


def create_user_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # Check if password and password confirmation match
        if password != password_confirm:
            return render(request, 'signup.html', {'error_message': 'Пароли не совпадают'})

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': 'Пользователь с таким логином уже существует'})
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html',
                          {'error_message': 'Пользователь с такой электронной почтой уже существует'})

        # Create user   
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return render(request, 'login.html')  # Render the form
    else:
        return render(request, 'signup.html')  # Render the form
