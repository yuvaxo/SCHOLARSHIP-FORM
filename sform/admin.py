

from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('s_code', 's_name', 'sex', 'dob', 'edu_year', 'f_m_name', 'community', 'p_income', 'ca_name', 'ia_name')
    search_fields = ('s_code', 's_name', 'community', 'ca_name', 'ia_name')
    list_filter = ('sex', 'edu_year', 'community')
    fieldsets = (
        (None, {
            'fields': ('s_code', 's_name', 'sex', 'dob', 'edu_year', 'f_m_name', 'community', 'p_income')
        }),
        ('Attachments', {
            'fields': ('community_attach', 'income_attach')
        }),
        ('Additional Info', {
            'fields': ('ca_name', 'ia_name', 'passwd')
        }),
    )

admin.site.register(Student, StudentAdmin)
