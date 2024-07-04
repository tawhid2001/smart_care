from django.contrib import admin
from .models import Doctor,AvailableTime,Specialization,Designation,Review

# Register your models here.

admin.site.register(Doctor)
admin.site.register(AvailableTime)
admin.site.register(Review)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}


admin.site.register(Designation,DesignationAdmin)
admin.site.register(Specialization,SpecializationAdmin)
