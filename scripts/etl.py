from pymongo import MongoClient
import psycopg2
from datetime import datetime

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017')
mongo_db = mongo_client['your_mongodb_database']
mongo_collection = mongo_db['your_mongodb_collection']

# Connect to PostgreSQL Data Warehouse
postgres_conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
)
postgres_cursor = postgres_conn.cursor()

# Function to transform and load data
def etl():
    for document in mongo_collection.find():
        donor = document.get('donor')
        recipient = document.get('recipient')
        contribution_amount = float(document.get('contribution_amount'))
        contribution_date = datetime.strptime(document.get('contribution_date'), "%Y-%m-%dT%H:%M:%S.%f").date()
        donor_type = document.get('donor_type')
        donor_address = document.get('donor_address')
        city_state_zip = document.get('city_state_zip')
        donor_reported_occupation = document.get('donor_reported_occupation')
        donor_reported_employer = document.get('donor_reported_employer')
        contribution_type = document.get('contribution_type')
        date_reported = datetime.strptime(document.get('date_reported'), "%Y-%m-%dT%H:%M:%S.%f").date()
        report_filed = document.get('report_filed')
        view_report_url = document.get('view_report', {}).get('url', '')
        transaction_id = document.get('transaction_id')
        retrieved_date = document.get('retrieved_date', {}).get('$date', '')

        # Load into PostgreSQL
        postgres_cursor.execute("""
            INSERT INTO Donors (Donor, Donor_Type, Donor_Address, City_State_Zip, Donor_Reported_Occupation, Donor_Reported_Employer)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (Donor) DO NOTHING;
        """, (donor, donor_type, donor_address, city_state_zip, donor_reported_occupation, donor_reported_employer))

        postgres_cursor.execute("""
            INSERT INTO Recipients (Recipient)
            VALUES (%s)
            ON CONFLICT (Recipient) DO NOTHING;
        """, (recipient,))

        postgres_cursor.execute("""
            INSERT INTO Dates (Contribution_Date, Contribution_Year)
            VALUES (%s, %s)
            ON CONFLICT (Contribution_Date) DO NOTHING;
        """, (contribution_date, contribution_date.year))

        postgres_cursor.execute("""
            INSERT INTO Contribution_Types (Contribution_Type)
            VALUES (%s)
            ON CONFLICT (Contribution_Type) DO NOTHING;
        """, (contribution_type,))

        postgres_cursor.execute("""
            INSERT INTO Report_Types (Report_Filed)
            VALUES (%s)
            ON CONFLICT (Report_Filed) DO NOTHING;
        """, (report_filed,))

        postgres_cursor.execute("""
            INSERT INTO Contributions (Transaction, Recipient, Contribution_Date, Contribution_Amount, Donor,
                                       Contribution_Type, Report_Filed, View_Report)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (Transaction) DO NOTHING;
        """, (transaction_id, recipient, contribution_date, contribution_amount, donor, contribution_type,
              report_filed, view_report_url))

    postgres_conn.commit()

# Run ETL
etl()

# Close connections
mongo_client.close()
postgres_cursor.close()
postgres_conn.close()
