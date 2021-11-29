from django.contrib import admin

from home.models import Paciente, tessiu

class PacienteAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Paciente,PacienteAdmin)

class tessiuAdmin(admin.ModelAdmin):
    list_display=('temperature','color','inflammation')
    search_fields=('temperature',)
# Register your models here.
admin.site.register(tessiu, tessiuAdmin)