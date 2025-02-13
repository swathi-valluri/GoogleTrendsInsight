from pytrends.request import TrendReq

def fetch_trends(keywords, timeframe="today 12-m", geo=""):
    pytrends = TrendReq()
    pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)
    return pytrends.interest_over_time()

if __name__ == "__main__":
    keywords = ["AI", "Machine Learning"]
    df = fetch_trends(keywords)
    print(df.head())
