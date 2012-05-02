from OVC_App.logbookShifts.models import Requester, Logbook, Phone, Mail
from django.contrib import admin


class LogbookAdmin(admin.ModelAdmin):
        list_display = ('b_date','b_time','e_time','delta_time','request')
        date_hierarchy = ('b_request')

admin.site.register(Logbook,LogbookAdmin)
admin.site.register(Requester)
admin.site.register(Phone)
admin.site.register(Mail)
