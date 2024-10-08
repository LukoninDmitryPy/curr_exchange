from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import requests

app = FastAPI()

@app.get("/api/rates")
async def get_exchange_rate(
    from_currency: str = Query(..., alias="from"),
    to_currency: str = Query(...,alias='to'),
    value: float = Query(..., alias='value'),
):
    try:
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
        data = response.json()
        exchange_rate = data["rates"][to_currency]
        result = value * exchange_rate
        return {"result": round(result, 2)}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Error fetching exchange rate")
    except KeyError:
        raise HTTPException(status_code=400, detail="Invalid currency code")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
