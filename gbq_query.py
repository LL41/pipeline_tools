import os
from google.cloud import bigquery
import pandas as pd

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ENTER_CREDENTIAL_PATH_HERE'
#To create a new key go here https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#client-libraries-install-python

client = bigquery.Client()

# Perform a query.
QUERY = (
    '''
--Insert Query here.
    ''')
query_job = client.query(QUERY)  # API request
df = query_job.to_dataframe() # Waits for query to finish

print(df)