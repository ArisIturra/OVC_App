from OVC_App.logbookShifts.models import Requester, Logbook, Phone, Mail
from django.contrib import admin


from reportlab.pdfgen import canvas
from django.http import HttpResponse

#-------------------------------------------

#admin.site.disable_action('delete_selected')
class LogbookAdmin(admin.ModelAdmin):
        list_display = ('b_date','author','b_time','e_time','delta_time','request','solution',)
        date_hierarchy = ('b_request')

	actions = ['get_required_time',]#'export_sumary']


	def save_model(self, request, obj, form, change):
        	obj.author = request.user
        	obj.save()	

	def get_required_time(self, request, q):
		import datetime
		d = {}	
		for v in q:
		
			try:
				d[str(v.author)] += v.delta_time()
			except KeyError:
				d[str(v.author)] = datetime.timedelta(0, 0)	
				d[str(v.author)] += v.delta_time()
		
		for r in d:
			self.message_user(request, "%s\t%s" %(r,d[r]))

	def export_sumary(self, request, q):
		# Create the HttpResponse object with the appropriate PDF headers.
	

		from django.contrib.admin.models import LogEntry
		from django.contrib.contenttypes.models import ContentType
		date = '%s al %s'%(q[0].b_request.date(),q.reverse()[0].b_request.date())
		

		print date
		for v in q:
			a = LogEntry.objects.first(object_repr=v)
			print a
				

#		response = HttpResponse(mimetype='application/pdf')
#    		response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'	
#    		p = canvas.Canvas(response)
#    		p.setLineWidth(.3)
#		p.setFont('Times-Roman', 16)
#		p.drawString(270,750,'Informe Turnos')
#		p.setFont('Times-Roman-Bold', 12)
#		p.drawString(270,700,'Informe Turnos')
#		p.showPage()
#		p.save()	
		

		self.message_user(request, "%s" % 'done')
#		return response
	export_sumary.short_description = "Export"
	

admin.site.register(Logbook,LogbookAdmin)
admin.site.register(Requester)
admin.site.register(Phone)
admin.site.register(Mail)
