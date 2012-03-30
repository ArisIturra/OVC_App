from OVC_App.Aditional_Rest.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

class RecessAdmin(admin.ModelAdmin):
	
	fieldsets = [
		(None, {'fields':[
				('user','resolution'),
				('resolution_date','recess','available_days'),
				],
			}
		),
		(_('Resolution Details'),{'fields':[
					('from_date','to_date','resolution_days',),
						],
					}
		),
		]

	list_display = ('user',	'resolution','resolution_date','recess','available_days')
	date_hierarchy = 'resolution_date'
	list_filter = ['user','resolution']


class RecessRequestAdmin(admin.ModelAdmin):


	def render_change_form(self, request, context, *args, **kwargs):
		self.change_form_template = 'admin/Aditional_Rest/recessrequest/change_form.html'

		ruser = RutUser.objects.get(user=request.user)
	        extra = {
			'ruser': ruser,
			'available_days': ruser.get_available_days()
      		}

        	context.update(extra)
		return super(RecessRequestAdmin, self).render_change_form(request, context,args, kwargs)

    	def queryset(self, request):
        	"""Limit Pages to those that belong to the request's user."""
        	qs = super(RecessRequestAdmin, self).queryset(request)
        	if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            		return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
		ruser = RutUser.objects.get(user=request.user)
        	return qs.filter(user=ruser)

	def save_model(self, request, obj, form, change):
		ruser = RutUser.objects.get(user=request.user)
		obj.user = ruser
        	obj.save()

admin.site.register(RutUser)
admin.site.register(Recess,RecessAdmin)
admin.site.register(RecessRequest,RecessRequestAdmin)

