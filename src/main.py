from service_functions import readFile, getCars, getRentals,\
    calculPrice, writeFile, invoice, getOptions


def main():
    # Get data from JSON file
    data = readFile("../data/lv_5_input.json")

    # Extrait data
    listCars = {}
    listRentals = {}
    listOptions = {}
    listCars = getCars(data)
    listRentals = getRentals(data)
    listOptions = getOptions(data)

    # Calcul rental price
    rentals = []

    for r in listRentals:
        bill = {}
        options = []

        # Get rental's options
        for opt in listOptions:
            option = listOptions.get(opt)

            if option.rental_id == r:
                options.append(option.type)

        rental = listRentals.get(r)
        price_details = calculPrice(
            rental, listCars.get(rental.car_id), options)
        bill["id"] = rental.id
        bill["options"] = options
        bill["actions"] = invoice(price_details)
        rentals.append(bill)

    # write to json file
    output = {"rentals": rentals}
    writeFile(output)


if __name__ == "__main__":
    main()