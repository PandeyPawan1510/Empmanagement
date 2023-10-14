from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExpenseModel(models.Model):
    expense_amount=models.IntegerField()
    expense_type = models.CharField(max_length=30)
    expense_date = models.DateField()
    expense_description = models.TextField(max_length=30)
    User=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    class Meta:
        db_table="expense"

def __str__(s):
    return s.User.username


