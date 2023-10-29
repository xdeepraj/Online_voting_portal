from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'id_card_no']
    ordering = ('email',)
    search_fields = ('email', 'first_name', 'id_card_no')
    
    # for editing user information from admin
    fieldsets = (
        ('Personal', {'fields': ('email', 'first_name', 'last_name', 'id_card_no',
                                 'mobile_no', 'address', 'profile_image',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )

    # for creating user from admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'id_card_no', 'mobile_no', 'address',
                       'profile_image', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
