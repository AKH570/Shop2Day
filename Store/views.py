from django.shortcuts import render
from django.http import HttpResponse
#from Inventory.models import PRODUCT
from Category.models import CATEGORY
from Inventory.models import PRODUCTS,STOCKS,SUBCATEGORY,BRAND
from django.core.paginator import Paginator
from django.db.models import Sum


# Create your views here.

def Inventory(request):
    totalStocks=STOCKS.objects.aggregate(total=Sum('stocks_qty'))
    #sum = sum(stocks.values_list('stocks_qty',flat=True))
    context = {
        'totalSt':totalStocks
    }
    print(f'stockTotal:{totalStocks}')
    return render(request,'store/inventory.html',context)

