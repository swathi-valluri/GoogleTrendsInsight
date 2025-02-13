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
    plt.close()

def plot_bar_chart(df, keywords, filename="bar_chart.png"):
    """Generates and saves a bar chart comparing keyword popularity."""
    if df.empty:
        print("No data available for visualization.")
        return

    avg_interest = df.mean()  # Compute average interest over time

    plt.figure(figsize=(8, 5))
    sns.barplot(x=avg_interest.index, y=avg_interest.values, palette="viridis")

    plt.xlabel("Keywords")
    plt.ylabel("Average Search Interest")
    plt.title("Average Google Search Interest Comparison")
    plt.xticks(rotation=45)

    # Save the plot as an image file
    image_path = os.path.join(OUTPUT_FOLDER, filename)
    plt.savefig(image_path)
    print(f"Bar chart saved as: {image_path}")
    plt.close()

def plot_heatmap(df, keywords, filename="heatmap.png"):
    """Generates and saves a heatmap for regional interest."""
    if df.empty:
        print("No data available for heatmap.")
        return

    plt.figure(figsize=(12, 6))
    sns.heatmap(df, cmap="coolwarm", annot=True, fmt=".0f", linewidths=0.5)

    plt.xlabel("Keywords")
    plt.ylabel("Region")
    plt.title("Google Trends Regional Interest")

    # Save the heatmap
    image_path = os.path.join(OUTPUT_FOLDER, filename)
    plt.savefig(image_path)
    print(f"Heatmap saved as: {image_path}")
    plt.close()