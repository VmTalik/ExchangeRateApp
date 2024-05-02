from django.contrib import admin

from .models import ExchangeRate


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('charcode', 'date', 'rate')
    list_filter = ('charcode', 'date')
    search_fields = ('charcode', 'date')
