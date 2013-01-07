from OVC_App.Aditional_Rest.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

class RecessAdmin(admin.ModelAdmin):
	
	fieldsets = [
		(None, {'fields':[
				('user','resolution'),
				('resolution_date','recess_days',),
				],
			}
		),
		(_('Resolution Details'),{'fields':[
					('from_date','to_date','resolution_days',),
						],
					}
		),
		]

	list_display = ('user',	'resolution','resolution_date','recess_days','used_days')
	date_hierarchy = 'resolution_date'
	list_filter = ['user','resolution']


class RecessRequestAdmin(admin.ModelAdmin):

#	list_display = ('user','begin','end','requested_days','halfday','status')
	list_display = ('user','begin','end','requested_days','halfday','status',)
	list_filter = ['user','status']
	def render_change_form(self, request, context, *args, **kwargs):
		self.change_form_template = 'admin/Aditional_Rest/recessrequest/change_form.html'

		ruser = Employee.objects.get(user=request.user)
		print ruser
	        extra = {
			'ruser': ruser,
			'recess_days': ruser.recess_days
      		}

        	context.update(extra)
		return super(RecessRequestAdmin, self).render_change_form(request, context,args, kwargs)

	def changelist_view(self, request, extra_context=None):

		emp = Employee.objects.get(user=request.user)
		print ACTIONS_CHOICES
		if emp.accions == STATUS_CHOICES['Admin']:
			self.list_filter = ['user','status']
		else: 
			self.list_filter = ['status']

		
		return super(RecessRequestAdmin,self).changelist_view(request, extra_context=None)

	def save_model(self, request, obj, form, change):
		emp = Employee.objects.get(user=request.user)
		obj.user = emp
		print emp
	       	obj.save()

 #   	def queryset(self, request):
 #       	"""Limit Pages to those that belong to the request's user."""

 #       	qs = super(RecessRequestAdmin, self).queryset(request)

  #      	if request.user.is_superuser:
   #         		return qs


#		ruser = RutUser.objects.get(user=request.user)
 #       	return qs.filter(user=ruser)

class EmployeeAdmin(admin.ModelAdmin):
#	list_display = ('user','recess_days','grade','cost_center','residence','legal_grade')
	pass	

#admin.site.register(RutUser)

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Recess,RecessAdmin)
admin.site.register(RecessRequest,RecessRequestAdmin)

