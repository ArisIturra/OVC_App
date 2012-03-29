from OVC_App.Aditional_Rest.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

class RecessAdmin(admin.ModelAdmin):
	
	fieldsets = [
		(None, {'fields':[
				('user','resolution'),
				('date','recess'),
				],
			}
		),
		(_('Resolution Details'),{'fields':[
					('from_date','to_date','resolution_days'),
						],
					}
		),
		]

	list_display = ('user',	'resolution','date','recess')
	date_hierarchy = 'date'
	list_filter = ['user','resolution']


class RecessRequestAdmin(admin.ModelAdmin):


	def render_change_form(self, request, context, *args, **kwargs):
		self.change_form_template = 'admin/Aditional_Rest/recessrequest/change_form.html'

	        extra = {
			'ruser': RutUser.objects.get(user=request.user)
      		}

        	context.update(extra)
		return super(RecessRequestAdmin, self).render_change_form(request, context,args, kwargs)




admin.site.register(RutUser)
admin.site.register(Recess,RecessAdmin)
admin.site.register(RecessRequest,RecessRequestAdmin)

