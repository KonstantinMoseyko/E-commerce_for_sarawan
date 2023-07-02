from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email', 
                    'is_staff', 'is_active', 'date_joined', 'avatar', 'age',)


admin.site.register(CustomUser, CustomUserAdmin)
