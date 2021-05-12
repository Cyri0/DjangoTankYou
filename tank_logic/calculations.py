
def calculate_average_quantity(events):
    if len(events) < 1:
        return None
    counter = 0
    quantity = 0
    for event in events:
        counter += 1
        quantity += event.petrol_quantity_liter
    return quantity / counter

def calculate_average_price(events):
    if len(events) < 1:
        return None
    counter = 0
    price = 0
    for event in events:
        counter += 1
        price += event.price_ft
    return price / counter

def calculate_consumption(events):
    try:
        last = events[0]
        before = events[1]
    except:
        return None
    return round(last.petrol_quantity_liter * 100/(last.km - before.km), 1)

def getElementFromEvents(events, index):
    try: 
        event = events[index]
        return event
    except:
        return None

def sum_price(events):
    if len(events) < 1:
        return None
    price = 0
    for event in events:
        price += event.price_ft
    return price