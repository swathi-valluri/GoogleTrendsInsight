import sys
import os

# Add the project root to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, request, jsonify
from trends.fetcher import fetch_trends, fetch_regional_interest

app = Flask(__name__)

@app.route('/api/trends', methods=['GET'])
def get_trends():
    """Fetch Google Trends data via API."""
    keywords = request.args.get('keywords')
    timeframe = request.args.get('timeframe', 'today 12-m')
    geo = request.args.get('geo', '')

    if not keywords:
        return jsonify({"error": "Missing required parameter: keywords"}), 400

    keyword_list = [kw.strip() for kw in keywords.split(",")]
    df = fetch_trends(keyword_list, timeframe=timeframe, geo=geo)

    if df.empty:
        return jsonify({"error": "No trend data found"}), 404

    return jsonify(df.to_dict(orient="records"))

@app.route('/api/regional_trends', methods=['GET'])
def get_regional_trends():
    """Fetch Google Trends regional interest via API."""
    keywords = request.args.get('keywords')
    geo = request.args.get('geo', '')

    if not keywords:
        return jsonify({"error": "Missing required parameter: keywords"}), 400

    keyword_list = [kw.strip() for kw in keywords.split(",")]
    df = fetch_regional_interest(keyword_list, geo=geo)

    if df.empty:
        return jsonify({"error": "No regional trend data found"}), 404

    return jsonify(df.to_dict())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
