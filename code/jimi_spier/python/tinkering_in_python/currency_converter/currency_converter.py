# Jimi Spier
# currency_converter.py
# 20220914


# ----------------------Import------------------------------------------ #
import lib_currency_converter as lcc 


# ----------------------Program-Instructions---------------------------- #
print("\nYour choices are:\n")

for key in lcc.country_codes:
    print(f"{key} --> {lcc.country_codes[key]}")
print()



# ----------------------User-Data-Collect------------------------------- #
user_choice_currency = input("Convert US Dollar to what currency: ")
user_money_exchange = input("How much would you like to convert: ")
# ----------------------Processing-------------------------------------- #
user_money_exchange = float(user_money_exchange)

grand_total = lcc.is_exchange_math(user_choice_currency, user_money_exchange)

# ----------------------Final-Result------------------------------------ #

print(f"${user_money_exchange} converted is: {grand_total} {lcc.country_codes[user_choice_currency]}\n")