from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    JsonResponse
)
import openfoodfacts as off

from . import utils    

# Create your views here.
def fetchEAN(request, ean='no_override'):
    '''fetchEAN View serves cleaned OpenFoodFacts JSON for passed EAN-13

    Args:
        request (http_request obj): http request object
        ean (str, optional): ean-13 product number. Defaults to 'no_override'.

    Returns:
        django.http.JsonResponse: JsonResponse of cleaned OpenFoodFacts Response
    '''

    # check against eroneous ean input
    if ean == 'no_overide' or not utils.is_ean13(str(ean)):
        return HttpResponseBadRequest("None EAN passed")
    
    # fetch openfoodfacts response
    off_resp = off.products.get_product(str(ean))

    # clean openfoodfacts response data
    resp = utils.cleanOFFResponse(off_resp)

    # return json response obj
    return JsonResponse(resp)

def fetchList(request):
    return HttpResponse('List')

def fetchIndex(request):
    return HttpResponse('Index')