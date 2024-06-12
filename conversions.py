def get_rate(base, term):
    pair = base + term
    if pair in exchange_rates:
        return exchange_rates[pair]
    inverted_pair = term + base
    if inverted_pair in exchange_rates:
        return 1 / exchange_rates[inverted_pair]
    return None

def convert(base_currency, term_currency, amount):
    rate = get_rate(base_currency, term_currency)
    if rate:
        return amount * rate
    else:
        cross_rate = cross_currency_conversion(base_currency, term_currency, amount)
        if cross_rate:
            return cross_rate
        else:
            raise ValueError(f"Unable to find rate for {base_currency}/{term_currency}")

def cross_currency_conversion(base_currency, term_currency, amount):
    if base_currency == "AUD" and term_currency == "JPY":
        aud_usd = get_rate("AUD", "USD")
        usd_jpy = get_rate("USD", "JPY")
        if aud_usd and usd_jpy:
            return amount * aud_usd * usd_jpy
    return None
