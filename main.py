import argparse
from trends.fetcher import fetch_trends, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch Google Trends data and save as CSV.")
    
    parser.add_argument(
        "--keywords", type=str, required=True,
        help="Comma-separated list of keywords (e.g., 'AI, Machine Learning')"
    )
    parser.add_argument(
        "--timeframe", type=str, default="today 12-m",
        help="Timeframe for trend analysis (e.g., 'today 12-m', '2020-01-01 2024-01-01')"
    )
    parser.add_argument(
        "--output", type=str, default="trends_output.csv",
        help="Output filename for CSV (default: trends_output.csv)"
    )

    args = parser.parse_args()
    
    keywords = [kw.strip() for kw in args.keywords.split(",")]
    df = fetch_trends(keywords, timeframe=args.timeframe)

    if not df.empty:
        print(df.head())
        save_to_csv(df, args.output)

if __name__ == "__main__":
    main()
