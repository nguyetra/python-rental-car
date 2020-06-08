class Car:
    """
    Class for a car

    Attributes:
        id (int): car ID
        price_per_day (int): car's price per day
        price_per_km (int): car's price per km
    """

    def __init__(self, id, price_per_day, price_per_km):
        """ 
        The constructor for Car class. 

        Parameters: 
           id (int): car ID
           price_per_day (int): car's price per day
           price_per_km (int): car's price per km
        """
        self.id = id
        self.price_per_day = price_per_day
        self.price_per_km = price_per_km


class Rental:
    """
    Class for a rental

    Attributes:
        id (int): car rental ID
        car_id (int): rented car's ID
        start_date (datetime): car rental start date
        end_date (datetime): car rental end date
        distance (int): approximate trip disance
    """

    def __init__(self, id, car_id, start, end, dist):
        """ 
        The constructor for Rental class. 

        Parameters: 
            id (int): car rental ID
            car_id (int): rented car's ID
            start_date (datetime): car rental start date
            end_date (datetime): car rental end date
            distance (int): approximate trip disance
        """
        self.id = id
        self.car_id = car_id
        self.start_date = start
        self.end_date = end
        self.distance = dist


class Option:
    """
    Class for an option bought after booking

    Attributes:
        id (int): option ID
        rental_id (int): rental ID
        type (str): option's type
    """

    def __init__(self, id, rental_id, type):
        """
        The constructor for Option class

        Parameters:
            id (int): option ID
            rental_id (int): rental ID
            type (str): option's type
        """
        self.id = id
        self.rental_id = rental_id
        self.type = type
