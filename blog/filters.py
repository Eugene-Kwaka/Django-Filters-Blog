import django_filters
from django_filters import DateTimeFromToRangeFilter, ChoiceFilter, CharFilter

from .models import Order

STATUS = (
    ('Pending', 'Pending'),
    ('Out for delivery', 'Out for delivery'),
    ('Delivered', 'Delivered'),
)

CATEGORY = (
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor'),
)


class OrderFilter(django_filters.FilterSet):
    product= CharFilter(field_name='product', lookup_expr='icontains')
    status = ChoiceFilter(choices=STATUS)
    category = ChoiceFilter(choices=CATEGORY)
    date_created = DateTimeFromToRangeFilter(
                  widget=django_filters.widgets.RangeWidget(
                  attrs={'type': 'date'}
    ))

    class Meta:
        model = Order
        fields = [
            'product',
            'category',
            'status',
            'date_created'
        ]