from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'booked_at', 'is_active')
    list_filter = ('is_active', 'booked_at')
    search_fields = ('user__username', 'session__class_type__name')
