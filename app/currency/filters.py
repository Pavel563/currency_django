import django_filters
from django.forms import DateInput

from currency.models import Rate


class RateFilter(django_filters.FilterSet):
    # created_gte = django_filters.DateFilter(
    #     widget=DateInput(attrs={'type': 'date'}),
    #     field_name='created', lookup_expr='date__gte',
    # )
    # created_lte = django_filters.DateFilter(
    #     widget=DateInput(attrs={'type': 'date'}),
    #     field_name='created', lookup_expr='date__lte',
    # )
    # created_lte = django_filters.DateFilter(
    #     field_name='created',
    #     lookup_expr='date__lte',
    #     widget=DateInput(attrs={'type': 'date'}),
    # )

    class Meta:
        model = Rate
        fields = {
            'buy': ('exact', ),
            # 'buy': ('lt', 'lte', 'gt', 'gte', 'exact'),
            'sale': ('exact', ),
            # 'sale': ('lt', 'lte', 'gt', 'gte', 'exact'),
            # 'type': ('in', ),
            # 'created': ('lte', 'gte'),
            # 'created_lte': (),
        }
