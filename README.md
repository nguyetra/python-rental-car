# python-rental-car 
Mini project in Python to calculate the amount for renting a car.

## Intro
From the quote for the rental car and the customer's booking information found in `data/lv_X_input.json`, write code that generates a `out/lv_X_output.json` contaning price of each rental.

The calculation method varies by level. Each level requires a different input and output file. The code source is stoken in `src` :
- `main.py` is the main function to run
- `service_functions.py` containing functions used by `main.py`
- `model.py` containing classes

## Running 
- Running `$python3 main.py` from folder `src` to get the result in `out/lv_X_output.json`

## Note
- All prices are stored as integers (in cents)
- Consult the commits to find the resolution of different levels ( one commit per level )

## Author
- Linh Nguyen
