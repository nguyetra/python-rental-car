import json
import datetime
from model import Car, Rental


def readFile(path):
    """Get data from JSON file
    
        Parameter:
            path (str): path to JSON file
        
        Return:
            Dict[str, str]: Dictionary of information about cars and rentals
    """
    try:
        with open(path) as f_in:
            return json.load(f_in)
    finally:
        f_in.close()


def writeFile(output):
    """Write data to JSON file
    
        Parameter:
            output (str) : list of rentals prices and its ID
        
        Return:
            file : file output.json containing the rental prices
    """
    try:
        with open("../out/lv_2_output.json", 'w', encoding='utf-8') as f_out:
            json.dump(output, f_out, indent=2)
    finally:
        f_out.close



def getCars(data):
    """Get information about cars
    
        Parameters: 
            data (Dict[str, str]) : Dictionary of information about cars and rentals

        Return:
            Dict[int, Car] : Dictionary of cars orders by car's ID
    """
    listCars = {}

    for c in data["cars"]:
        if (c['id'] is None or c['price_per_day'] is None or
                c['price_per_km'] is None):
            print("Cars : Unfound info \n")
            return
        else:
            if (type(c['id']) != int or
                type(c['price_per_day']) != int or
                    type(c['price_per_km']) != int):
                print("Cars : Invalide type \n")
                return
            else:
                car = Car(c['id'], c['price_per_day'], c['price_per_km'])
                listCars[car.id] = car
    return listCars



def getRentals(data):
    """Get information about rentals
    
        Parameters: 
            data (Dict[str, str]) : Dictionary of information about cars and rentals

        Return:
            Dict[int, Rental] : Dictionary of rentals orders by rental's ID
    """
    listRentals = {}

    for r in data["rentals"]:
        if (r['id'] is None or r['car_id'] is None or
            r['start_date'] is None or r['end_date'] is None or
                r['distance'] is None):
            print("Rentals : Unfound info! \n")
            return
        else:
            if (type(r['id']) != int or
                type(r['start_date']) != str or
                type(r['end_date']) != str or
                    type(r['distance']) != int):
                print("Rentals : Invalide type \n")
                return
            else:
                format_str = '%Y-%m-%d'
                start = datetime.datetime.strptime(r['start_date'], format_str)
                end = datetime.datetime.strptime(r['end_date'], format_str)

                rental = Rental(r['id'], r['car_id'],
                                start, end, r['distance'])
                listRentals[rental.id] = rental

    return listRentals


def calculPrice(rental, car):
    """ Calcul the price of each rental
        Lv2 : Having a decreasing pricing for longer rentals
            - price per day decreases by 10% after 1 day
            - price per day decreases by 30% after 4 days
            - price per day decreases by 50% after 10 days
     
        Parameters: 
            rental (Rental): Class Rental's object contaning information about the rental
            car (Car): Class Car's object contaning information about the car
  
        Return: 
            int: Rental price in cents 
    """
    days = (rental.end_date - rental.start_date).days + 1
    days_price = 0

    for d in range(days):
        if d >= 10:
            days_price += car.price_per_day * 0.5
        elif d >= 4:
            days_price += car.price_per_day * 0.7
        elif d >= 1:
            days_price += car.price_per_day * 0.9
        else:
            days_price += car.price_per_day

    return int(days_price) + rental.distance * car.price_per_km
