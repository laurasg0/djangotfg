from django.contrib import admin
from .models import ClassType, ClassSession

@admin.register(ClassType)
class ClassTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'id_center')
    search_fields = ('name',)

@admin.register(ClassSession)
class ClassSessionAdmin(admin.ModelAdmin):
    list_display = ('class_type', 'date', 'start_time', 'end_time', 'max_capacity', 'is_active')
    list_filter = ('is_active', 'date', 'class_type')
    search_fields = ('class_type__name',)
