
import argparse
from trends import fetcher
from trends.visualizer import plot_trends, plot_bar_chart, plot_heatmap
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Fetch and visualize Google Trends data.")
    
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
        help="Output filename for CSV or JSON (default: trends_output.csv)"
    )
    parser.add_argument(
        "--visualize", action="store_true",
        help="Enable visualization and save as image files"
    )
    parser.add_argument(
        "--heatmap", action="store_true",
        help="Generate and save a heatmap for regional interest"
    )
    parser.add_argument(
        "--geo", type=str, default="",
        help="Specify country code for regional analysis (e.g., 'US', 'IN', 'GB')"
    )

    args = parser.parse_args()
    
    keywords = [kw.strip() for kw in args.keywords.split(",")]
    df = fetcher.fetch_trends(keywords, timeframe=args.timeframe)

    if not df.empty:
        print(df.head())
        fetcher.save_to_file(df, args.output)  # Now saves both CSV & JSON

        if args.visualize:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            line_chart_filename = f"trend_{timestamp}.png"
            bar_chart_filename = f"bar_chart_{timestamp}.png"
            
            plot_trends(df, keywords, filename=line_chart_filename)
            plot_bar_chart(df, keywords, filename=bar_chart_filename)

    if args.heatmap:
        regional_df = fetcher.fetch_regional_interest(keywords, geo=args.geo)
        if not regional_df.empty:
            heatmap_filename = f"heatmap_{timestamp}.png"
            plot_heatmap(regional_df, keywords, filename=heatmap_filename)

if __name__ == "__main__":
    main()
