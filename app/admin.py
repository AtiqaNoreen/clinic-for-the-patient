
# Register your models here.
from django.contrib import admin
from .models import Doctor, Appointment

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'experience', 'rating', 'status')
    list_filter = ('status', 'specialty')
    search_fields = ('name', 'specialty')

admin.site.register(Appointment)  