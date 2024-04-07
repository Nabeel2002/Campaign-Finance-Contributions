import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB connection settings
# Replace "<connection string>" with your Atlas connection string
MONGODB_URI = "mongodb+srv://nabeel:<Nabeel>@austindata.2cnp26f.mongodb.net/?retryWrites=true&w=majority&appName=AustinData"
DB_NAME = "AustinData"
COLLECTION_NAME = "Contributions"

# API endpoint
API_ENDPOINT = "https://data.austintexas.gov/resource/3kfv-biw6.json"

def fetch_data_from_api():
    try:
        response = requests.get(API_ENDPOINT)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data from API. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred while fetching data from API:", e)
        return None

def store_data_in_mongodb(data):
    try:
        client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        result = collection.insert_many(data)
        print("Data successfully stored in MongoDB. Inserted IDs:", result.inserted_ids)
    except Exception as e:
        print("An error occurred while storing data in MongoDB:", e)

def main():
    data = fetch_data_from_api()
    if data:
        store_data_in_mongodb(data)

if __name__ == "__main__":
    main()
