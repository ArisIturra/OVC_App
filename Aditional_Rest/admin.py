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




admin.site.register(RutUser)
admin.site.register(Recess,RecessAdmin)
admin.site.register(RecessRequest)

# Re-register UserAdmin
#admin.site.unregister(User)
#admin.site.register(User, MyUserAdmin)



