from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .models import AuthorizationToken


class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        # list_display is used to create the 'Display users / Select user to change' form in Django administration
        'phone_no', 'first_name', 'last_name', 'date_of_birth', 'user_type', 'is_active'
    )
    list_filter = (
        # list_filter is used to create filters in 'Display users / Select user to change' form in Django administration
        'user_type', 'is_active'
    )
    fieldsets = (
        # add_fieldsets is used to create the 'Change user' form in Django administration
        (None, {'fields': ('phone_no', 'password', 'user_type',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'county', 'locality', 'email', )}),
        ('Status', {'fields': ('is_active', )})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        # add_fieldsets is used to create the 'Add user' form in Django administration
        (None, {
            'classes': ('wide',),
            'fields': ('phone_no', 'user_type', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth',
                       'county', 'locality', 'email', ),
        }),
    )
    search_fields = ('phone_no', 'first_name', 'last_name',)
    ordering = ('last_name',)
    list_per_page = 100
    filter_horizontal = ()


class AuthorizationTokenAdmin(admin.ModelAdmin):
    fields = ['code', 'expiry']
    list_display = ['token', 'code', 'expiry']
    list_filter = []
    search_fields = ['code']
    ordering = ('-expiry',)
    list_per_page = 100

    def has_add_permission(self, request, obj=None):
        """
        It could be helpful to modify a code for an existing token, but not add a new token
        """
        return False


admin.site.register(AuthorizationToken, AuthorizationTokenAdmin)
admin.site.register(User, UserAdmin)

# Not using Django's built-in permissions. Unregister the Group model from admin.
admin.site.unregister(Group)
