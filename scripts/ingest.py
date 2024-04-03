import requests
import datetime
from pymongo import MongoClient

# API for the dataset
api_url = "https://data.austintexas.gov/resource/3kfv-biw6.json"

# MongoDB connection details
client = MongoClient("mongodb://localhost:27017")
db = client["austin_campaign_finance"]
collection = db["contributions"]

# Function to retrieve data from API
def get_data():
    response = requests.get(api_url)
    data = response.json()
    return data

# Function to store data in MongoDB
def store_data(data):
    for item in data:
        #data transformation
        item["retrieved_date"] = datetime.datetime.now()  # Add retrieval date
        collection.insert_one(item)

# Retrieve data from API
data = get_data()

# Store data in MongoDB
store_data(data)

print("Data stored successfully!")
