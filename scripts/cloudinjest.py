import requests
from pymongo import MongoClient
import urllib.parse

# API endpoint
api_url = "https://data.austintexas.gov/resource/3kfv-biw6.json"

# MongoDB credentials
username = "xzy1551"
password = urllib.parse.quote_plus("Nabeel2002")  # URL encode the password
cluster_address = "austincontributions.3qvgojq.mongodb.net"
database_name = "AustinContributions"
collection_name = "Contributions"

# Construct MongoDB connection URI
mongo_uri = f"mongodb+srv://{username}:{password}@{cluster_address}/{database_name}?retryWrites=true&w=majority&appName=AustinContributions"

def fetch_data(api_url):
    """Fetch data from the API endpoint."""
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an error on bad status
    return response.json()

def insert_data_to_mongodb(data, mongo_uri, database_name, collection_name):
    """Insert data into MongoDB collection."""
    # Create a MongoDB client
    client = MongoClient(mongo_uri)
    # Select the database
    db = client[database_name]
    # Select the collection
    collection = db[collection_name]
    # Insert the data into the collection
    if data:  # Ensure there's data to insert
        collection.insert_many(data)
    else:
        print("No data to insert")

def main():
    # Fetch data from the API
    data = fetch_data(api_url)
    print(f"Fetched {len(data)} records from the API")
    # Insert data into MongoDB
    insert_data_to_mongodb(data, mongo_uri, database_name, collection_name)
    print("Data inserted into MongoDB successfully")

if __name__ == "__main__":
    main()
