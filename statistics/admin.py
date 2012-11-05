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

class EvaluationAdmin(admin.ModelAdmin):

        fieldsets = [
                (None, {'fields':['date','hour']}),
                (None, {'fields':['station','choice']}),
        ]
        list_display = ('station','date','hour','choice')
        list_filter = ['station','choice']
        date_hierarchy = 'date'
        save_as = True


admin.site.register(Station)
admin.site.register(Evaluation,EvaluationAdmin)
admin.site.register(Choice,ChoiceAdmin)

