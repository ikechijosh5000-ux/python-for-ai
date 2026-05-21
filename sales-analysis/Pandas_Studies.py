import pandas as pd


sales_data = pd.read_json("sales-analysis/output/sales_data.json")
weather_report= pd.read_csv("data/paris_weather.csv")
type (sales_data["date"])
sales_data["date"].shape

sales_data.head(5)

sales_data.tail(5)

weather_report.head(5)

weather_report.tail(5)

weather_report.dtypes
sales_data.dtypes

sales_data.to_excel("output/sales_with_totals.xlsx", sheet_name ="date", index = False)

sales_data = pd.read_excel("output/sales_with_totals.xlsx", sheet_name = "date")

weather_report.to_excel("../lagos_weather.xlsx", sheet_name ="date", index = False)

weather_report = pd.read_excel("../lagos_weather.xlsx", sheet_name = "date")

weather_report["date"]
weather_report ["max_temp"]
type(weather_report["date"])
weather_report["date"].shape
date_min_temp = weather_report[['date', 'min_temp']]
type(date_min_temp)
weather_report[['date', 'min_temp']].shape
weather_report.head()
