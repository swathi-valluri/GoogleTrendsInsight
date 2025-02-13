
# 📊 GoogleTrendsInsight - Google Trends API & Visualization 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
![Docker Pulls](https://img.shields.io/docker/pulls/swathival/googletrendsinsight)


## **🚀Overview**
GoogleTrendsInsight is an open-source API that fetches and visualizes **Google Trends** data.  
This API helps users **analyze search trends over time** and **compare keyword popularity** across regions.

## **📌 Features**
✅ Fetch **Google Trends data** via API  
✅ Compare multiple **keywords over time**  
✅ Retrieve **regional search interest**  
✅ **Export data** in **CSV & JSON** formats  
✅ **Docker support** for easy deployment  

---

## **📌 Installation Instructions**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/YOUR-USERNAME/GoogleTrendsInsight.git
cd GoogleTrendsInsight
````

### **2️⃣ Set Up a Virtual Environment**

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

### **4️⃣ Run the Flask API Locally**

```sh
python web/api.py
```

✅ API will be available at:

```
http://127.0.0.1:5000
```

## Usage

### CLI Usage
```shell
python main.py --keywords "machine learning, AI, blockchain" --timeframe "today 12-m" --output "output.csv" --visualize --heatmap --geo "US"
```

---

## **📌 Running with Docker**

### **1️⃣ Build the Docker Image**

```sh
sudo docker build -t googletrendsinsight .
```

### **2️⃣ Run the Container**

```sh
sudo docker run -p 5000:5000 googletrendsinsight
```

✅ The API will now be running inside Docker.

---

## **📌 API Usage**

### **1️⃣ Fetch Google Trends Data**

```sh
curl "http://localhost:5000/api/trends?keywords=AI%2CBlockchain&timeframe=today%2012-m"
```

📌 **Expected Output (JSON)**

```json
[
  {"AI": 61, "Blockchain": 1},
  {"AI": 64, "Blockchain": 1},
  {"AI": 60, "Blockchain": 1}
]
```

### **2️⃣ Fetch Regional Interest**

```sh
curl "http://localhost:5000/api/regional_trends?keywords=AI%2CBlockchain&geo=US"
```

📌 **Expected Output (JSON)**

```json
{
  "California": {"AI": 80, "Blockchain": 15},
  "New York": {"AI": 75, "Blockchain": 20}
}
```

---

## **📌 Contributing**

🚀 Contributions are welcome! To contribute:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature-name`)
3. **Commit your changes** (`git commit -m "Added new feature"`)
4. **Push to GitHub** and **submit a pull request!**

---

## **📌 License**

📜 This project is licensed under the **MIT License**.

---
