from service_functions import readFile, getCars, getRentals, calculPrice, writeFile


def main():
    # Get data from JSON file
    data = readFile("../data/lv_1_input.json")

    # Extrait data
    listCars = {}
    listRentals = {}
    listCars = getCars(data)
    listRentals = getRentals(data)

    # Calcul rental price
    rentals = []

    for r in listRentals:
        bill = {}
        rental = listRentals.get(r)
        price = calculPrice(rental, listCars.get(rental.car_id))
        bill["id"] = rental.id
        bill["price"] = price
        rentals.append(bill)

    # write to json file
    output = {"rentals": rentals}
    writeFile(output)


if __name__ == "__main__":
    main()