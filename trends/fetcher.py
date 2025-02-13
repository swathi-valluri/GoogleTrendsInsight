import time
import pandas as pd
from pytrends.request import TrendReq

def fetch_trends(keywords, timeframe="today 12-m", geo=""):
    pytrends = TrendReq()
    time.sleep(5)  # Prevents rapid requests to Google Trends

    pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)
    df = pytrends.interest_over_time()
    
    if not df.empty:
        df = df.drop(columns=["isPartial"])  # Remove unnecessary column
        df = df.infer_objects(copy=False)  # Fix future warning

    return df

def save_to_csv(df, filename="trends_output.csv"):
    if df.empty:
        print("No data to save.")
        return
    df.to_csv(filename, index=True)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    keywords = ["AI", "Machine Learning"]
    df = fetch_trends(keywords)
    if not df.empty:
        print(df.head())
        save_to_csv(df, "trends_output.csv")
