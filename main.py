from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException
import pandas as pd

## GLOBAL VARS
id_cols = ['acct', 'owner_2024', 'address_2024', 'city_2024', 'tot_mkt_val_2024', 'tot_mkt_val_2023', 
           'yr_built_2024', 'yr_remodel_2024', 'bed_2024', 'bed_2023', 'bath_2024', 'bath_2023', 
           'stories_2024', 'stories_2023']
group_cols = ['tot_mkt_val_2023_bin', 'neighborhood_grp_2024', 'neighborhood_grp_2023', 
              'bld_grade_2024', 'bld_grade_2023', 'yr_built_2024_bin', 'yr_remodel_2024_bin', 
              'bed_2024_bin', 'bed_2023_bin', 'bath_2024_bin', 'bath_2023_bin', 
              'stories_2024_bin', 'stories_2023_bin']

app = FastAPI()
master = pd.read_parquet('https://sfc-project-files.s3.amazonaws.com/tx-data/hc-property-taxes/master.gzip')

def get_address_data(master, address: str, city: str) -> Dict[str, Any]:
    """Fetches address-related property data."""

    address = address.upper()
    city = city.upper()

    acct_info = master[(master["address_2024"] == address) & (master["city_2024"] == city)]

    if acct_info.empty:
        raise HTTPException(status_code=404, detail="No data found for the given address and city.")

    data = {
        "About this home": acct_info[id_cols].to_dict(orient="records")[0],
        "Matching criteria (group 1)": acct_info[["group1_id"] + group_cols].to_dict(orient="records")[0],
        "Result (group 1)": acct_info[['tot_mkt_val_pctchange', 'group1_typical_mkt_val_pctchange']].to_dict(orient="records")[0],
        "Matches (group 1)": master[master["group1_id"] == acct_info["group1_id"].iloc[0]][id_cols].to_dict(orient="records"),
    }

    return data

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_address_data")
def fetch_address_data(address: str, city: str):
    """API endpoint to retrieve property data by address and city."""
    return get_address_data(master, address, city)
