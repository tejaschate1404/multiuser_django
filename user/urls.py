from django.urls import path
from .views import signup, login_view, logout_view, admin_dashboard, employee_dashboard, hr_dashboard, reference_person_dashboard

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('employee_dashboard/', employee_dashboard, name='employee_dashboard'),
    path('hr_dashboard/', hr_dashboard, name='hr_dashboard'),
    path('reference_person_dashboard/', reference_person_dashboard, name='reference_person_dashboard'),
]
