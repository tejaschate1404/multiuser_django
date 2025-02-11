from django.contrib import admin
from .models import HRProfile
from .models import EmployeeProfile
from .models import ReferencePersonProfile

# Register your models here.

admin.site.register(HRProfile)
admin.site.register(EmployeeProfile)
admin.site.register(ReferencePersonProfile)