from django.contrib import admin
from .models import ExpenseModel
class ExpenseSchema(admin.ModelAdmin):
    list_display=["User","id","expense_amount","expense_type","expense_date","expense_description"]
# Register your models here.


admin.site.register(ExpenseModel,ExpenseSchema)
