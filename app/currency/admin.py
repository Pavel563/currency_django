from django.contrib import admin

from rangefilter.filters import DateTimeRangeFilter

from currency.models import Rate, Bank, ContactUs

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class RateResource(resources.ModelResource):

    class Meta:
        model = Rate


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        'id',
        'type',
        'buy',
        'sale',
        'created',
        'bank',
    )
    list_filter = (
        ('created', DateTimeRangeFilter),
        'type',
        'bank',
        'created',
    )
    search_fields = (
        'type',
        'bank',
    )
    readonly_fields = (
        'buy',
        'sale',
    )

    # def has_delete_permission(self, request, obj=None):
    #     return False



class BankResource(resources.ModelResource):

    class Meta:
        model = Bank

class BankAdmin(ImportExportModelAdmin):
    resource_class = BankResource
    list_display = (
        'id',
        'name',
        'url',
        )


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
        'message',
        )
    readonly_fields = (
        'id',
        'email_from',
        'subject',
        'message',
    )

    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False

admin.site.register(Rate, RateAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(ContactUs, ContactUsAdmin)