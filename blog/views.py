from django.shortcuts import render
from .models import Order
from .filters import OrderFilter
# Create your views here.
def index(request):
    orders = Order.objects.all().order_by('-date_created')
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {
        'orders': orders,
        'myFilter': myFilter,
    }
    return render(request, 'index.html', context)
