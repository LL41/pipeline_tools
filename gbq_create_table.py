import pandas as pd
import pandas_gbq

#Replace PROJECT
project_id = "PROJECT"

#Replace DATASET.TABLE
table_id = 'DATASET.TABLE'

df = pd.DataFrame()

pandas_gbq.to_gbq(df, table_id, project_id=project_id)