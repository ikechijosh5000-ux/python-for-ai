import os

# This keeps running even if file doesn't exist
try:
    with open("sales-analysis/output/sales_data.json", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Could not find data.txt")
    content = "default data"
print("Done!")  # Always reaches here

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "data/weather_chart.png"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")
