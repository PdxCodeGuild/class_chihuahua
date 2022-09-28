# Jimi Spier
# lib_currency_converter.py
# 20220914

# ----------------------Dictionary-------------------------------------- #

exchange_rates = {
    "eur": 1.002311,
    "pnd": 0.866809,
    "aus": 1.484234,
    "cad": 1.318053,
    "spd": 1.406474,
    "yen": 143.192347,
    "mex": 19.976858
}

country_codes = {
    "eur": "Euros",
    "pnd": "Pounds",
    "aus": "Australian Dollars",
    "cad": "Canadian Dollars",
    "spd": "Singapore Dollars",
    "yen": "Japanese Yen",
    "mex": "Mexican Pesos" 
}
# ----------------------Function---------------------------------------- #
def is_exchange_math(user_choice="", user_amount=0.00):
    exchange_total = exchange_rates[user_choice] * user_amount
    exchange_total_rnd = round(exchange_total,2)
    return exchange_total_rnd
    