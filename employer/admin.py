from django.contrib import admin
# Register your models here.
from mptt.admin import MPTTModelAdmin


from .models import Employer


# Register your models here


admin.site.register(Employer, MPTTModelAdmin)

