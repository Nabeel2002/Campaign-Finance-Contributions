import pymongo
import pandas as pd

# MongoDB connection URI
uri = "mongodb+srv://xzy1551:Nabeel2002@austincontributions.3qvgojq.mongodb.net/?retryWrites=true&w=majority&appName=AustinContributions"

# Connect to the MongoDB cluster
client = pymongo.MongoClient(uri)

# Access the specific database and collection
db = client['AustinContributions']
collection = db['Contributions']

# Extract: Read data from MongoDB collection
data = list(collection.find())

# Transform: Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Drop MongoDB's default _id field as it's not needed for visualization
df.drop(columns=['_id'], inplace=True)

# Ensure 'contribution_amount' is numeric
df['contribution_amount'] = pd.to_numeric(df['contribution_amount'], errors='coerce')

# Transform dates to datetime format
df['contribution_date'] = pd.to_datetime(df['contribution_date'], errors='coerce')
df['date_reported'] = pd.to_datetime(df['date_reported'], errors='coerce')

# Add any additional transformations needed for visualizations
# Split 'city_state_zip' into separate columns with more robust handling
city_state_zip_split = df['city_state_zip'].str.rsplit(', ', n=2, expand=True)

# If the split results in three parts, we have city, state, and zip
if city_state_zip_split.shape[1] == 3:
    df['city'] = city_state_zip_split[0]
    df['state'] = city_state_zip_split[1]
    df['zip'] = city_state_zip_split[2]
# If the split results in two parts, we may only have city and state/zip
elif city_state_zip_split.shape[1] == 2:
    df['city'] = city_state_zip_split[0]
    state_zip_split = city_state_zip_split[1].str.split(' ', n=1, expand=True)
    df['state'] = state_zip_split[0]
    df['zip'] = state_zip_split[1]
else:
    df['city'] = city_state_zip_split[0]
    df['state'] = ''
    df['zip'] = ''

# Clean up whitespace in 'zip'
df['zip'] = df['zip'].str.strip()

# Drop the original 'city_state_zip' column
df.drop(columns=['city_state_zip'], inplace=True)

# Load: Save the transformed data into a CSV file
df.to_csv('Austin_ready_data.csv', index=False)

print("ETL process completed successfully. Data saved to Austin_ready_data.csv")
