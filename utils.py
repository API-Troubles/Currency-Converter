# A seperated space for utility functions, keeps main.py more organized!
from thefuzz import process


def convert_symbol(text: str, currency_options: dict) -> str:
    if text not in list(currency_options.keys()):
        return list(currency_options.keys())[list(currency_options.values()).index(text)]
    return text


def find_match(orignal: str, options: dict) -> str:
    match, confidence = process.extractOne(orignal, options) # type: ignore
    if confidence < 90:
        raise ValueError(f"No currency found for '{orignal}'. Did you mean '{match}'?")
    return match