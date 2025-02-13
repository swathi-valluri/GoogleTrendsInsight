# GoogleTrendsInsight


## Overview
GoogleTrendsInsight is an open-source tool for visualizing Google Trends data with interactive charts and CSV export functionality. It helps users analyze keyword trends over time, compare multiple search terms, and gain insights into search interest across different regions.

## Features
- Fetch Google Trends data for user-provided keywords
- Generate interactive visualizations (line charts, heatmaps, bar charts)
- Compare search trends for multiple keywords
- Export trend data as CSV for further analysis
- Simple CLI for quick analysis
- Web interface for interactive data exploration (Planned)

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/YOUR-USERNAME/GoogleTrendsInsight.git
   cd GoogleTrendsInsight
   ```
2. **Set Up Virtual Environment**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### CLI Usage (Initial Version)
```sh
python main.py --keywords "machine learning, AI, blockchain" --timeframe "today 12-m"
```

### Web UI (Planned)
1. Start the Flask/FastAPI server
2. Access the web interface via `http://localhost:5000`

## Roadmap
- [ ] Implement CLI for fetching Google Trends data
- [ ] Add CSV export functionality
- [ ] Build visualization modules for trend insights
- [ ] Develop a web-based UI for interactive analysis
- [ ] Deploy as a Docker container

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

 
