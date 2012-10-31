from OVC_App.statistics.models import *
from django.contrib import admin
from statistics import customfields



#-------------------------------------------

#admin.site.disable_action('delete_selected')
        
class ChoiceAdmin(admin.ModelAdmin):
        list_display = ('details','name','weight')
        formfield_overrides = {
                ColorChoiceField:{'widget':customfields.ColorWidget}
        }



admin.site.register(Station)
admin.site.register(Evaluation)
admin.site.register(Choice,ChoiceAdmin)

