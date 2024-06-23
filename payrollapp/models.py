from django.db import models


class EmpAttendence(models.Model):
    empno=models.IntegerField()
    month=models.CharField(max_length=100)
    days_present=models.IntegerField()

    def __str__(self):
        return f"{self.empno}"
    

    def get_empno(ids):
        return EmpAttendence.objects.all()

class BasicPayofmonth(models.Model):
    empno = models.IntegerField()
    basic_pay = models.IntegerField()

    def __str__(self):
        return f"{self.empno}"
    
class IncomeTax(models.Model):
    empno = models.IntegerField()
    it_perc=models.IntegerField()

    def __str__(self):
        return f"{self.empno}"
    