from .models import Values
from django.contrib import admin


@admin.register(Values)
class BulkAdmin(admin.ModelAdmin):
    list_display = ('euro_dol',
                    'brl_dol',
                    'jpy_dol',
                    'of_date',
                    'created_at')
