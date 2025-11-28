from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserSession

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'name', 'surname', 'role', 'membership_level')
    list_filter = ('role', 'membership_level', 'gender')
    search_fields = ('username', 'email', 'name', 'surname')
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('name', 'surname', 'phone', 'birthdate', 'gender')}),
        ('Rol y membresía', {'fields': ('role', 'reward_points', 'membership_level')}),
    )

@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'token_session', 'start_date', 'last_connection', 'end_date')
    list_filter = ('start_date',)
    search_fields = ('id_user__username', 'token_session')
