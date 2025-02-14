import time
import random
import pandas as pd
import requests
from pytrends.request import TrendReq
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

MAX_RETRIES = 5
MAX_KEYWORDS = 5  # Limit to avoid Google blocking

def create_session():
    """Creates a requests session with retry strategy for handling 429 errors."""
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=0.2,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    return session

def fetch_trends(keywords, timeframe="today 12-m", geo=""):
    """Fetches Google Trends data with rate limiting and retry logic."""
    if len(keywords) > MAX_KEYWORDS:
        print(f"⚠️ Too many keywords! Reduce to {MAX_KEYWORDS} or fewer to avoid rate limiting.")
        return pd.DataFrame()
    
    session = create_session()
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.requests = session  # Assign session manually

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            sleep_time = random.uniform(15, 30)  # Increased delay to reduce 429 errors
            print(f"🕒 Waiting {sleep_time:.2f} seconds before requesting data (Attempt {attempt})...")
            time.sleep(sleep_time)

            pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)  # ✅ Fixed missing timeframe
            df = pytrends.interest_over_time()

            if not df.empty:
                df = df.drop(columns=["isPartial"], errors="ignore")
                df = df.infer_objects(copy=False)  # Ensure correct data types
            return df

        except Exception as e:
            print(f"⚠️ Error fetching trends (Attempt {attempt}/{MAX_RETRIES}): {e}")
            time.sleep(2 ** attempt)  # ✅ Exponential backoff (2, 4, 8, 16 seconds)

    print("❌ Failed to fetch trends after multiple attempts.")
    return pd.DataFrame()

def fetch_regional_interest(keywords, geo=""):
    """Fetches Google Trends interest by region with rate limiting."""
    if len(keywords) > MAX_KEYWORDS:
        print(f"⚠️ Too many keywords! Reduce to {MAX_KEYWORDS} or fewer.")
        return pd.DataFrame()
    
    session = create_session()
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.requests = session  # Assign session manually

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            sleep_time = random.uniform(10, 20)  # Increased delay to reduce 429 errors
            print(f"🕒 Waiting {sleep_time:.2f} seconds before regional data request (Attempt {attempt})...")
            time.sleep(sleep_time)

            pytrends.build_payload(keywords, geo=geo)
            df = pytrends.interest_by_region()

            if not df.empty:
                df = df.infer_objects(copy=False)  # Fix FutureWarning
            return df

        except Exception as e:
            print(f"⚠️ Error fetching regional interest (Attempt {attempt}/{MAX_RETRIES}): {e}")
            time.sleep(2 ** attempt)  # ✅ Exponential backoff (2, 4, 8, 16 seconds)

    print("❌ Failed to fetch regional interest after multiple attempts.")
    return pd.DataFrame()

def save_to_file(df, filename="trends_output"):
    """Saves data in multiple formats (CSV & JSON)."""
    if df.empty:
        print("❌ No data to save.")
        return

    # Ensure the filename has an extension, if not, save both CSV & JSON
    if "." not in filename:
        csv_filename = f"{filename}.csv"
        json_filename = f"{filename}.json"

        df.to_csv(csv_filename, index=True)
        df.to_json(json_filename, orient="records", indent=4)

        print(f"✅ Data saved as {csv_filename} and {json_filename}")
    else:
        # If a specific extension is provided, save accordingly
        if filename.endswith(".csv"):
            df.to_csv(filename, index=True)
        elif filename.endswith(".json"):
            df.to_json(filename, orient="records", indent=4)
        else:
            print("⚠️ Unsupported file format. Use .csv or .json")
            return
        
        print(f"✅ Data saved as {filename}")
