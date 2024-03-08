from . models import CATEGORY
from Inventory.models import SUBCATEGORY

def categoryLink(request):
    Catglinks = CATEGORY.objects.all().exclude(slug__in=['popular','new-arrival','popular-item'])
    sublinks  = SUBCATEGORY.objects.filter(category__in=Catglinks)
    return dict(catglinks=Catglinks,
        sublinks=sublinks,)
# def subcategoryLink(request):
#     links=SUBCATEGORY.objects.all()
#     return dict(subcatlinks=links)