from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import ast

# Define allowed origins
origins = [
    "http://localhost:8000",  # React/Vue/Angular running locally
    "https://localhost:8000", 
    "http://127.0.0.1:8000",   # Alternative local address
    "https://127.0.0.1:8000",
    "http://127.0.0.1:8081",   # Alternative local address
    "https://127.0.0.1:8081",
    "https://www.houstonchronicle.com/",  # Deployed frontend
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_address_data(address: str, city: str, zip: int) -> Dict[str, Any]:
    """Fetches address-related property data."""

    address = address.upper().strip()
    city = city.upper().strip()

    master = pd.read_parquet(f'https://sfc-project-files.s3.amazonaws.com/tx-data/hc-property-taxes/matches_{zip}.gzip')
    columns = master.columns
    acct_info = master[(master["address"].str.contains(address)) & (master["city"] == city)].iloc[0]
    matches = ast.literal_eval(acct_info['matches'])
    matches = [{columns[i+1]: m[i] for i in range(len(columns[:-3]))} for m in matches]

    if acct_info.empty:
        raise HTTPException(status_code=404, detail="No data found for the given address.")

    data = {
        "About this home": acct_info[columns[:-1]].to_dict(),
        # "Matching criteria (group 1)": acct_info[["group1_id"] + group_cols].to_dict(orient="records")[0],
        # "Result (group 1)": acct_info[['tot_mkt_val_pctchange', 'tot_mkt_val_pctchange_adj', 'group1_typical_mkt_val_pctchange']].to_dict(orient="records")[0],
        "Matches:": matches[0]
    }

    return data


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_address_data")
def fetch_address_data(address: str, city: str, zip: int):
    """API endpoint to retrieve property data by address and city."""
    return get_address_data(address, city, zip)
