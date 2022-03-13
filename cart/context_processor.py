from . models import *
from . views import *
from django.core.exceptions import ObjectDoesNotExist


def count(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct=cartlist.objects.filter(cartid=cid(request))
            cti=items.objects.all().filter(cart=ct[:1])
            for c in cti:
                item_count += c.quan
        except cartlist.DoesNotExist:
            item_count=0
        return dict(itc=item_count)
