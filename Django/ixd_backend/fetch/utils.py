
import re
import requests

def is_ean13(string):
    '''checks string for is EAN-13 type

    Args:
        string (str): EAN-13 contender

    Returns:
        bool: is-ean-13
    '''
    return bool(re.match(r"^\d{13}$", string))

def cleanOFFResponse(off_resp):
    '''cleanOFFResponse prunes extraneous fields from openfoodfacts response json

    Args:
        off_resp (JSON): OpenFoodFacts response JSON

    Returns:
        JSON: Pruned JSON
    '''
    return off_resp

def _baseUrl(api_version):
    '''_baseUrl returns OpenFoodFacts API base Url

    Args:
        api_version (int): api version to be querries

    Returns:
        string: full base url for open food facts api
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

