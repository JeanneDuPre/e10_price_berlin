import pytankerkoenig
import datetime
import json
import os
import pandas as pd

API_KEY = os.environ['API_KEY']
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Load the existing dataset (if it exists)
existing_data_file = "data/tankstellen_price_Stand.json"
if os.path.exists(existing_data_file):
    with open(existing_data_file, "r") as infile:
        existing_data = json.load(infile)
    df_existing = pd.DataFrame(existing_data)
else:
    df_existing = pd.DataFrame()

# Fetch new data
new_data = pytankerkoenig.getNearbyStations(API_KEY, '52.4819479', '13.3213254', '4', 'all', 'dist')
new_data['scraping_datetime'] = current_time  # Add a column with scraping datetime
new_data_df = pd.DataFrame(new_data)

# Append the new data to the existing dataset
df_combined = pd.concat([df_existing, new_data_df], ignore_index=True)

# # Save the updated dataset
# with open(existing_data_file, "w") as outfile:
#     outfile.write(df_combined.to_json(orient='records', lines=True))
# Save the updated dataset
with open(existing_data_file, "w") as outfile:
    for _, row in df_combined.iterrows():
        outfile.write(json.dumps(row.to_dict()) + '\n')
