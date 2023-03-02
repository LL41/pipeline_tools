from google.cloud import bigquery

#Construct a BigQuery client object.
#Specify project to query from. Check gbq_query file to setup credentials locally.
client = bigquery.Client(project='YOUR_PROJECT')

#Set TABLE_ID to the ID of the destination table.
table_id = "TABLE_ID"

job_config = bigquery.QueryJobConfig(destination=table_id)

sql = """
--Insert query here.
"""

# Start the query, passing in the extra configuration.
query_job = client.query(sql, job_config=job_config)  # Make an API request.
query_job.result()  # Wait for the job to complete.

print(f"Query results loaded to the table {table_id}".)