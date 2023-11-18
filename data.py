import pandas as pd
import os
import re

def read_and_process_files():
    directory_path = "../data/raw/"  # Modify this to your directory path containing the JSON files
    file_paths = [os.path.join(directory_path, filename) for filename in os.listdir(directory_path) if filename.endswith(".json")]

    all_dfs = []

    for file_path in file_paths:
        try:
            # Extract datetime from the file name using regular expressions
            datetime_match = re.search(r'\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}', os.path.basename(file_path))

            if datetime_match:
                datetime_string = datetime_match.group()
                file_datetime = pd.to_datetime(datetime_string, format='%Y-%m-%d_%H-%M-%S')
            else:
                # Handle the case when the filename format doesn't match
                file_datetime = None

            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()
                df = pd.read_json(data)
                
            # Extract data inside the 'stations' column
            stations_data = pd.json_normalize(df['stations'])

            # Select the desired columns from the extracted data
            stations_data['file_datetime'] = file_datetime
            stations_data['date'] = pd.to_datetime(stations_data['file_datetime']).dt.date
            stations_data['time'] = pd.to_datetime(stations_data['file_datetime']).dt.strftime('%H:%M:%S')

            all_dfs.append(stations_data)
        except Exception as e:
            print(f"Error reading file: {file_path}. Error: {e}")

    resulting_dataframe = pd.concat(all_dfs, ignore_index=True)
    resulting_dataframe = resulting_dataframe[resulting_dataframe['name'] != 'Avus']
    return resulting_dataframe
