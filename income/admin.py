from django.contrib import admin
from .models import IncomeModel
class IncomeSchema(admin.ModelAdmin):
    list_display=["User","id","income_amount","income_type","income_date","income_description"]

# Register your models here.
admin.site.register(IncomeModel,IncomeSchema)