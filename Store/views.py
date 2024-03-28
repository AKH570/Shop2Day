from django.shortcuts import render
from django.http import HttpResponse
#from Inventory.models import PRODUCT
from Category.models import CATEGORY
from Inventory.models import PRODUCTS,STOCKS,SUBCATEGORY,BRAND,PRICE
from django.core.paginator import Paginator
from django.db.models import Sum,F


# Create your views here.

def Inventory(request):
    totalStocks= STOCKS.objects.aggregate(total=Sum('stocks_qty'))
    totalStockPrice = PRICE.objects.values('stock').aggregate(
        total=Sum(F('storeprice')* F('stock__stocks_qty'))
    )
    print(f'stockprice:{totalStockPrice}')
    print(f'stock:{totalStocks}')
    context = {
        'totalSt':totalStocks,
        'stPrice':totalStockPrice,
    }
    # print(f'stockTotal:{totalStocks}')
    return render(request,'store/inventory.html',context)

