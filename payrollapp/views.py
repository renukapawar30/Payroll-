from django.shortcuts import render,HttpResponse
from .models import EmpAttendence,BasicPayofmonth,IncomeTax

def home(request):
    employee_numbers = EmpAttendence.objects.values_list('empno', flat=True).distinct()
    unique_months = EmpAttendence.objects.values_list('month', flat=True).distinct()
    
    if request.method == 'POST':
        empno = request.POST.get('empno')
        month = request.POST.get('month')
        
      
        attendance = EmpAttendence.objects.get(empno=empno, month=month)
        basic_pay = BasicPayofmonth.objects.get(empno=empno)
        income_tax = IncomeTax.objects.get(empno=empno)
        
       
        gross_pay = attendance.days_present * basic_pay.basic_pay
        
       
        net_pay = gross_pay - (gross_pay * (income_tax.it_perc / 100))
        
        context = {
            'employee_numbers': employee_numbers,
            'unique_months': unique_months,
            'gross_pay': gross_pay,
            'net_pay': net_pay
        }
        
        return render(request, 'index.html', context)
    
    context = {
        'employee_numbers': employee_numbers,
        'unique_months': unique_months,
    }
    
    return render(request, 'index.html', context)
