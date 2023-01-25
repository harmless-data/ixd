import re
import requests

def is_ean13(string):
    '''checks string for is EAN-13 type

    Args:
        string (str): EAN-13 contender

    Returns:
        bool: is-ean-13
    
    TODO:
        add None-String Parsing
        add divergent EAN Matching
        add differentiating return object
    '''
    return bool(re.match(r"^\d{13}$", string))

def cleanOFFResponse(off_resp):
    '''cleanOFFResponse prunes extraneous fields from openfoodfacts response json

    Args:
        off_resp (JSON): OpenFoodFacts response JSON

    Returns:
        JSON: Pruned JSON

    TODO:
        add pruning (function currently serves as pass-through stub)
    '''
    product_json = filter_json_fields(json_data=off_resp,fields=['product'])

    return off_resp

def _baseUrl(api_version):
    '''_baseUrl returns OpenFoodFacts API base Url

    Args:
        api_version (int): api version to be querries

    Returns:
        string: full base url for open food facts api

    TODO: 
        add local hosted option
    '''
    return f'https://world.openfoodfacts.org/api/v{api_version}'

def _getProduct(ean : str,api_version=2):
    '''_getProduct fetches JSON for ean-13 without sdk use

    Args:
        ean (str): ean-13 product number    
        api_version (int, optional): off api version. Defaults to 2.

    Returns:
        JSON: OpenFoodFacts response JSON
    '''
    
    url = f'{_baseUrl(api_version)}/product/{ean}.json'
    
    r = requests.get(url)
    
    return r.json() if r.status_code == 200 else {}

def filter_json_fields(json_data, fields):
    '''filter_json_fields takes json and returns only the given fields

    Args:
        json_data (JSON): JSON Object
        fields ([str]): List of Fields in JSON to keep

    Returns:
        JSON: Pruned JSON
    '''
    filtered_json = {key: json_data[key] for key in fields if key in json_data}
    return filtered_json

def spawn_filter_json(eans):
    pass

def palmOil_FILTER(json):
    pass

