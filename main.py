import json
import os

import currencyapicom
from thefuzz import process


def find_match(user_input: str, options: dict):
    match, confidence = process.extractOne(user_input, options)
    if confidence < 90:
        raise ValueError(f"No currency found for '{user_input}'. Did you mean '{match}'?")
    return match

# Opening JSON file
with open('test.json') as f:
    result = json.loads(f.read())

# You will need to replace this with your api key!
# api_key = os.environ['CURRENCY_API_KEY']

# client = currencyapicom.Client(api_key)

list_options = []

# result = client.currencies()
currencies = result["data"]
for item in currencies:
    currency = currencies[item]
    list_options.append(currency['name'])
    list_options.append(currency['symbol'])


orignal_currency = input("Currency to convert from: ")
result = find_match(orignal_currency, list_options)


print(result)