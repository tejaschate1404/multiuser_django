from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from .utils import role_required  # Import the decorator

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if CustomUser.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists."})

        user = CustomUser(username=username, email=email, role=role)
        user.password = make_password(password)
        user.save()

        login(request, user)
        return redirect_user_dashboard(user)

    return render(request, "signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect_user_dashboard(user)
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def redirect_user_dashboard(user):
    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'employee':
        return redirect('employee_dashboard')
    elif user.role == 'hr':
        return redirect('hr_dashboard')
    elif user.role == 'reference_person':
        return redirect('reference_person_dashboard')

@login_required
@role_required(allowed_roles=["admin"])
def admin_dashboard(request):
    return render(request, 'dashboards/admin.html', {'user': request.user})


@login_required
@role_required(allowed_roles=["employee"])
def employee_dashboard(request):
    return render(request, 'dashboards/employee_dashboard.html', {'user': request.user})

@login_required
@role_required(allowed_roles=["hr"])
def hr_dashboard(request):
    return render(request, 'dashboards/hr_dashboard.html', {'user': request.user})

@login_required
@role_required(allowed_roles=["reference_person"])
def reference_person_dashboard(request):
    return render(request, 'dashboards/reference_person_dashboard.html', {'user': request.user})
