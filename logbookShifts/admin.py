from OVC_App.logbookShifts.models import Requester, Logbook, Phone, Mail
from django.contrib import admin


from reportlab.pdfgen import canvas
from django.http import HttpResponse

#-------------------------------------------

#admin.site.disable_action('delete_selected')
class LogbookAdmin(admin.ModelAdmin):
        list_display = ('b_date','b_time','e_time','delta_time','request','solution')
        date_hierarchy = ('b_request')

	actions = ['export_sumary']
	
	def export_sumary(self, request, queryset):
		# Create the HttpResponse object with the appropriate PDF headers.
		response = HttpResponse(mimetype='application/pdf')
    		response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'	
		# Create the PDF object, using the response object as its "file."
    		p = canvas.Canvas(response)

    		p.setLineWidth(.3)
		p.setFont('Times-Roman', 16)
		
		p.drawString(270,750,'Informe Turnos')
		

		p.setFont('Times-Roman-Bold', 12)
		
		p.drawString(270,700,'Informe Turnos')

		
		p.showPage()
		p.save()	
		self.message_user(request, "%s" % 'done')
		return response
	export_sumary.short_description = "Export"
	

admin.site.register(Logbook,LogbookAdmin)
admin.site.register(Requester)
admin.site.register(Phone)
admin.site.register(Mail)
