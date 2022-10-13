from django.contrib import admin
from .models import Shop, Report

# Register your models here.
class ReportInline(admin.TabularInline):
    model = Report

class ShopAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ReportInline]

admin.site.register(Shop, ShopAdmin)