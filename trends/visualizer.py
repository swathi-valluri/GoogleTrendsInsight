import os
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure the output folder exists
OUTPUT_FOLDER = "visualizations"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def plot_trends(df, keywords, filename="trend_plot.png"):
    """Generates and saves a line chart for Google Trends data."""
    if df.empty:
        print("No data available for visualization.")
        return

    plt.figure(figsize=(12, 6))
    for keyword in keywords:
        if keyword in df.columns:
            plt.plot(df.index, df[keyword], label=keyword)

    plt.xlabel("Date")
    plt.ylabel("Search Interest")
    plt.title("Google Trends Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)

    # Save the plot as an image file
    image_path = os.path.join(OUTPUT_FOLDER, filename)
    plt.savefig(image_path)
    print(f"Visualization saved as: {image_path}")

    plt.close()  # Prevents interactive display issues
