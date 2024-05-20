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
# For example, we can split 'city_state_zip' into separate columns
df[['city', 'state', 'zip']] = df['city_state_zip'].str.split(', ', expand=True)
df['zip'] = df['zip'].str.split(',').str[1]  # To handle cases like "Austin, TX, 78746"

# Drop the original 'city_state_zip' column as we have split it into separate columns
df.drop(columns=['city_state_zip'], inplace=True)

# Load: Save the transformed data into a CSV file
df.to_csv('Austin_ready_data.csv', index=False)

print("ETL process completed successfully. Data saved to Austin_ready_data.csv")
