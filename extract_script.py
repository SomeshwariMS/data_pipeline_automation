import pandas as pd
import os
import logging

def extract_data(data_source):
    """
    Extract data from various sources.

    Parameters:
    - data_source: Dictionary containing information about the data source.
                   Example: {'file_path': 'path/to/your/data.csv', 'format': 'csv'}

    Returns:
    - pandas.DataFrame: Extracted data.
    """
    file_path = data_source.get('file_path')
    data_format = data_source.get('format')

    try:
        if data_format.lower() == 'csv':
            data = pd.read_csv(file_path)
        elif data_format.lower() == 'json':
            data = pd.read_json(file_path)
        else:
            raise ValueError(f"Unsupported data format: {data_format}")

        logging.info(f"Data extracted successfully from {file_path}.")
        return data

    except Exception as e:
        logging.error(f"Error during data extraction from {file_path}: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    logging.basicConfig(level=logging.INFO)  # Set logging level to INFO
    data_source = {'file_path': 'data/source_data.csv', 'format': 'csv'}
    
    extracted_data = extract_data(data_source)

    if extracted_data is not None:
        print("Data extracted successfully:")
        print(extracted_data.head())
    else:
        print("Data extraction failed.")
