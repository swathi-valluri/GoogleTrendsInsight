import time
import random
import pandas as pd
from pytrends.request import TrendReq

def fetch_trends(keywords, timeframe="today 12-m", geo=""):
    """Fetches Google Trends data for the given keywords with rate limiting."""
    pytrends = TrendReq()

    # Introduce a randomized delay to avoid rate limiting
    sleep_time = random.uniform(10, 20)  # Random delay between 5-10 seconds
    print(f"Waiting {sleep_time:.2f} seconds before requesting data...")
    time.sleep(sleep_time)

    pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)
    
    df = pytrends.interest_over_time()
    if not df.empty:
        df = df.drop(columns=["isPartial"], errors="ignore")  # Remove unnecessary column
        df = df.infer_objects(copy=False)  # Fix FutureWarning

    return df

def fetch_regional_interest(keywords, geo=""):
    """Fetches Google Trends interest by region for given keywords."""
    pytrends = TrendReq()

    # Introduce delay before making requests
    sleep_time = random.uniform(10, 20)
    print(f"Waiting {sleep_time:.2f} seconds before requesting regional data...")
    time.sleep(sleep_time)

    pytrends.build_payload(keywords, geo=geo)
    
    df = pytrends.interest_by_region()
    
    if not df.empty:
        df = df.infer_objects(copy=False)  # Ensure proper data types

    return df

def save_to_csv(df, filename="trends_output.csv"):
    """Saves the DataFrame as a CSV file."""
    if df.empty:
        print("No data to save.")
        return
    df.to_csv(filename, index=True)
    print(f"Data saved to {filename}")
