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

#	actions = ['get_report']

#	def get_report(self,request,q):
#		from statistics.reports import Report

#	        rep = Report()
#		data = rep.all()
#		print data
#		for ev in q:
#			for d in data:
#				print d

#class EvaluationAdmin(admin.ModelAdmin):

#        fieldsets = [
#                (None, {'fields':['date','hour']}),
#                (None, {'fields':['station','choice']}),
#        ]
#        list_display = ('station','date','hour','choice')
#        list_filter = ['station','choice']
#        date_hierarchy = 'date'
#        save_as = True

class StationAdmin(admin.ModelAdmin):

	list_display = ('name','longitude','latitude','elevation')


admin.site.register(Station,StationAdmin)
admin.site.register(Evaluation,EvaluationAdmin)
admin.site.register(Choice,ChoiceAdmin)

