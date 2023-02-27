from enum import Enum

class NutriScore(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'

def contains_ingredients_analysis_tag(json,tag : str):
    if 'ingredients_analysis_tags' in json['product'].keys():
        for _tag in json['product']['ingredients_analysis_tags']:
            if tag in _tag:
                return True
            return False
    
def filter_palm_oil_free(json) -> bool:
    '''filter_palm_oil_free _summary_

    Args:
        json (_type_): _description_

    Returns:
        bool: _description_
    '''
    return contains_ingredients_analysis_tag(json,'palm-oil-free')
            
def filter_fair_trade(json) -> bool:
    '''filter_fair_trade _summary_

    Args:
        json (_type_): _description_

    Returns:
        bool: _description_
    '''
    return 'Fairtrade International' in json['product']['labels']

def filter_bio(json) -> bool:
    '''filter_bio _summary_

    Args:
        json (_type_): _description_

    Returns:
        bool: _description_
    '''
    return 'Bio' in json['product']['labels']

def filter_vegan(json) -> bool:
    '''filter_vegan _summary_

    Args:
        json (_type_): _description_

    Returns:
        bool: _description_
    '''
    return contains_ingredients_analysis_tag(json,'vegan')

def filter_vegetarian(json) -> bool:
    '''filter_vegetarian _summary_

    Args:
        json (_type_): _description_

    Returns:
        bool: _description_
    '''
    return contains_ingredients_analysis_tag(json,'vegetarian')

def filter_low_food_processing(json) -> bool:
    '''filter_low_food_processing _summary_

    Args:
        json (_type_): _description_

    Returns:
        bool: _description_
    '''
    pass

def filter_nutri_score(json) -> NutriScore:
    '''filter_nutri_score _summary_

    Args:
        json (_type_): _description_

    Returns:
        NutriScore: _description_
    '''
    return json['product']['nutriscore_grade'] if 'nutriscore_grade' in json['product'].keys() else None

def filter_packaging(json):
    '''filter_packaging _summary_

    Args:
        json (_type_): _description_

    Returns:
        _type_: _description_
    '''
    return json['product']['packaging'] if 'packaging' in json['product'].keys() else None


def filter_transport(json):
    '''filter_transport _summary_

    Args:
        json (_type_): _description_
    '''
    pass

def filter_full_filtering(json):
    '''filter_full_filtering _summary_

    Args:
        json (_type_): _description_

    Returns:
        _type_: _description_
    '''
    return  {
        'palm-oil-free' : filter_palm_oil_free(json),
        'fair-trade' : filter_fair_trade(json),
        'bio' : filter_bio(json),
        'vegan' : filter_vegan(json), 
        'vegetarian' : filter_vegetarian(json),
        'low-food-processing' : filter_low_food_processing(json),
        'nutri-score' : filter_nutri_score(json),
        'packaging' : filter_packaging(json),
        'transport' : filter_transport(json),
            }
