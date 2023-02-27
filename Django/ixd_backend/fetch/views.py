from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    JsonResponse

)
from django.views.decorators.csrf import csrf_exempt

import openfoodfacts as off
import json

from . import utils    
from . import filters
from .models import StaticData

# Create your views here.
def fetchEAN(request, ean='no_override'):
    '''fetchEAN View serves cleaned OpenFoodFacts JSON for passed EAN-13

    Args:
        request (http_request obj): http request object
        ean (str, optional): ean-13 product number. Defaults to 'no_override'.

    Returns:
        django.http.JsonResponse: JsonResponse of cleaned OpenFoodFacts Response

    Endpoint:
        http://127.0.0.1:8000/fetch/EAN/3700214616970/

    '''

    # check against eroneous ean input
    # if ean == 'no_overide' or not utils.is_ean13(str(ean)):
    #     return HttpResponseBadRequest("None EAN passed")

    if ean == 'no_overide':
        return HttpResponseBadRequest("None EAN passed")

    if StaticData.objects.filter(ean=str(ean)).exists():
        # fetch object from db
        obj = StaticData.objects.get(ean=ean)

        # parse json from db object
        resp = obj.json
    else:
        # fetch openfoodfacts response
        off_resp = off.products.get_product(str(ean))

        # clean openfoodfacts response data
        resp = utils.cleanOFFResponse(off_resp)

    # return json response obj
    return JsonResponse(resp)

@csrf_exempt
def fetchList(request):
    '''fetchList fetches information for posted JSON containing Lsit of EAN-13

    Args:
        request (http_request obj): Http Request Object

    Returns:
        django.http.JsonResponse: List of JsonResponse of cleaned OpenFoodFacts Response
    '''

    # parse against eroneous request
    if request.method != 'POST':
        return JsonResponse({"error": "Invalid request method"})

    # parse json input
    json_data = request.body
    json_data = json.loads(json_data)

    # extract ean list
    eans = json_data['eans']

    # generate filtered response
    json_resp = {ean : utils.cleanOFFResponse(off.products.get_product(ean)) for ean in eans}

    return JsonResponse(json_resp)

def fetchIndex(request):
    return HttpResponse('Index')

def addToStatic(request,ean='no-override'):
    # fetch from OFF
    # save object ean refernce
    if ean == 'no-override':
        return HttpResponseBadRequest()

    _json = utils.cleanOFFResponse(off.products.get_product(str(ean)))
    new = StaticData(ean=ean,json=_json)
    new.save()
    return JsonResponse(_json)
