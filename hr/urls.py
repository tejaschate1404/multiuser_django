from django.urls import path
from .views import hr_page 
from .views import hr_signup, hr_login, hr_logout

urlpatterns = [
    path('hr_page/', hr_page, name='hr_page'),
    path('signup/', hr_signup, name='hr_signup'),
    path('login/', hr_login, name='hr_login'),
    path('logout/', hr_logout, name='hr_logout'),
]

