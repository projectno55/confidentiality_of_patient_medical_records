from django.contrib import admin
from service.models import *

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display=('name', 'gender', 'date_of_birth','aadharnumber','email','phonenumber','maritalstatus','bloodgroup',
           'address', 'symptoms','ename','relation', 'emergencynumber')
admin.site.register(Patient, PatientAdmin)

class ContactusAdmin(admin.ModelAdmin):
    list_display=('username', 'email', 'message')
admin.site.register(Contact, ContactusAdmin)

class FeedbacksAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'message')
admin.site.register(Feedback, FeedbacksAdmin)

def approve_apps(modeladmin, request, queryset):
    queryset.update(is_approved=True)

approve_apps.short_description = "Approve selected apps"

class AppAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'phoneNo', 'is_approved']

    def save_model(self, request, obj, form, change):
        # Check if the is_approved checkbox is checked in the admin form
        is_approved = form.cleaned_data.get('is_approved')

        if is_approved:
            obj.is_approved = True
            obj.save()
        else:
            # If not approved, you might want to take some other action or not save at all
            # For example, you can redirect the user to a rejection page or raise an exception
            pass
admin.site.register(Appointments, AppAdmin)