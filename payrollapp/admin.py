from django.contrib import admin

from .models import EmpAttendence,BasicPayofmonth,IncomeTax

class EmpAttendenceAdmin(admin.ModelAdmin):
    list_display = ('empno','month','days_present')

class BasicPayofmonthAdmin(admin.ModelAdmin):
    list_display = ('empno','basic_pay')

class IncomeTaxAdmin(admin.ModelAdmin):
    list_display = ('empno','it_perc')

admin.site.register(EmpAttendence,EmpAttendenceAdmin)
admin.site.register(BasicPayofmonth,BasicPayofmonthAdmin)
admin.site.register(IncomeTax,IncomeTaxAdmin)

#Username:payroll
#password:123