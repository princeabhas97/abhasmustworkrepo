from django.contrib import admin
from mustworkApp.models import test2
# Register your models here.
#admin.site.register(test2)
@admin.register(test2)
class TransactionDetailAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email')
    list_per_page = 20
    search_fields = ['email',]