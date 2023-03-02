import os
from google.cloud import bigquery
import pandas as pd

#Below are steps to run this file locally. GOOGLE_APPLICATION_CREDENTIALS are not needed when running from cloud shell editor or other Google enviroments.
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ENTER_CREDENTIAL_PATH_HERE'
#To create a new key go here https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#client-libraries-install-python
#client = bigquery.Client()

#Fill in LOCATION_OF_DATASET and GBQ_PROJECT below if using in google enviroment.
client = bigquery.Client(location = 'LOCATION_OF_DATASET', project='GBQ_PROJECT')

# Perform a query.
QUERY = (
    '''
--Paste query here.
    ''')
query_job = client.query(QUERY)  # API request
df = query_job.to_dataframe() # Waits for query to finish

print(df)