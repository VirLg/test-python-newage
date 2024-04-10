import gspread
import pandas_gbq
from google.oauth2.service_account import Credentials

credentials = Credentials.from_service_account_file('creds.json')
gc = gspread.service_account(filename='creds.json')
query = """
    SELECT event_date, user_pseudo_id, event_name, geo.country,device.category
    FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_20210131` 
    LIMIT 100
"""
df = pandas_gbq.read_gbq(query, project_id='dark-forge-419813', credentials=credentials)

# dataFrame
wks = gc.open("test")
worksheet = wks.worksheet("dataFrame")
worksheet.update([df.columns.values.tolist()] + df.values.tolist())

# count unique event name 
countName = df["event_name"].value_counts()
workOne = wks.worksheet("CountEvent")
workOne.update([countName.index.tolist()] + [countName.values.tolist()])

unique = df["user_pseudo_id"].nunique()
data_to_update = [[unique]]

workTwo = wks.worksheet("UniqueId")

workTwo.update('A1:B1', [["uniqe id", unique]]) 