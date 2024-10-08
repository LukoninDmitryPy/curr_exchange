# Exchange Rate API

A simple API for fetching exchange rates.

## Endpoints
------------

### GET /api/rates

Returns the exchange rate for a given currency pair.

#### Query Parameters

* `from`: The base currency (e.g. USD, EUR, JPY)
* `to`: The target currency (e.g. USD, EUR, JPY)
* `value`: The amount to convert (e.g. 1, 100, 500, 1000)

#### Response

* `result`: The converted amount (rounded to 2 decimal places)

#### Example Request

```bash
GET /api/rates?from=USD&to=EUR&value=100
```
