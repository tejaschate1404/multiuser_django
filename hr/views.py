from django.shortcuts import render
from django.http import HttpResponse
from user.utils import role_required  # Import the decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
@role_required(allowed_roles=["hr"])
def hr_page(request):
    return HttpResponse("hello tejas")



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user.models import CustomUser, HRProfile
from django.contrib import messages

# HR Signup View
def hr_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        company_name = request.POST['company_name']
        image = request.FILES.get('image')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('hr_signup')

        # Create HR User
        user = CustomUser.objects.create_user(username=username, email=email, password=password, role='hr')
        HRProfile.objects.create(user=user, company_name=company_name, image=image)

        messages.success(request, "HR account created successfully! Please log in.")
        return redirect('hr_login')

    return render(request, 'hr_signup.html')


# HR Login View
def hr_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.role == 'hr':
            login(request, user)
            return redirect('hr_dashboard')  # Redirect to HR dashboard
        else:
            messages.error(request, "Invalid credentials or you are not an HR user.")
            return redirect('hr_login')

    return render(request, 'hr_login.html')


# HR Logout View
def hr_logout(request):
    logout(request)
    return redirect('hr_login')
