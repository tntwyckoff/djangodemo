
def imperial_bmi (weight, height):
    # bmi calc: needs weight (pounds), height (inches)
    mWeight = convert_imperial_pounds_to_kg (weight)
    mHeight = convert_imperial_inches_to_meters (height)
    return metric_bmi (mWeight, mHeight)

def metric_bmi (weight, height):
    # bmi calc: weight over square of height:
    return weight / (height ** 2)
    
def convert_imperial_pounds_to_kg (weight):
    return weight * 0.453592

def convert_imperial_inches_to_meters (height):
    return height * 0.0254

