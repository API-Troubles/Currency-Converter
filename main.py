import json
import os

import currencyapicom

from utils import convert_symbol, find_match

# You will need to replace this with your api key!
api_key = os.environ['CURRENCY_API_KEY']
# ^ Insert API key here ^ (Remove the os.environ)

client = currencyapicom.Client(api_key)
currency_options: dict[str, str] = {}
currency_api = client.currencies()

# Get all supported currencies
currencies = currency_api["data"]
for item in currencies:
    currency = currencies[item]
    currency_options[currency['code']] = currency['name']


orignal_currency = input("Currency to convert from: ")
amt = input("How much currency? ")
new_currency = input("Currency to convert into: ")

# Value checks
try:
    amt = int(amt)
except ValueError:
    raise ValueError("The currency amount must be a number!") from None


# Gets all symbols from the {symbol, name} dict by going thru
# each (key, value) pair, and adds the key and value in list
symbols = [item for pair in currency_options.items() for item in pair]

orignal_currency = find_match(orignal_currency, symbols) # type: ignore
new_currency = find_match(new_currency, symbols) # type: ignore


# Convert names to symbol if name for API
from_symbol = convert_symbol(orignal_currency, currency_options)
into_symbol = convert_symbol(new_currency, currency_options)



result = client.latest(base_currency=[from_symbol], currencies=[into_symbol])
conversion = result["data"][into_symbol]["value"]*amt

print("Your currency conversion:")
print(f"{amt} {from_symbol} => {round(conversion, 3)} {into_symbol}")