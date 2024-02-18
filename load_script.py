import pandas as pd
import logging
from sqlalchemy import create_engine

def load_data(data, destination):
    """
    Load transformed data into the specified destination.

    Parameters:
    - data: pandas.DataFrame, Transformed data to be loaded.
    - destination: Dictionary containing information about the destination.
                   Example: {'type': 'csv', 'file_path': 'path/to/your/output.csv'}
                            or
                            {'type': 'database', 'engine_string': 'postgresql://user:password@localhost:5432/your_database',
                             'table_name': 'your_table'}

    Returns:
    - None
    """
    destination_type = destination.get('type')

    try:
        if destination_type.lower() == 'csv':
            file_path = destination.get('file_path')
            data.to_csv(file_path, index=False)
            logging.info(f"Data loaded successfully to CSV: {file_path}")

        elif destination_type.lower() == 'database':
            engine_string = destination.get('engine_string')
            table_name = destination.get('table_name')
            engine = create_engine(engine_string)
            data.to_sql(table_name, con=engine, index=False, if_exists='replace')
            logging.info(f"Data loaded successfully to Database: {table_name}")

        else:
            logging.warning(f"Unsupported destination type: {destination_type}. Skipping.")

    except Exception as e:
        logging.error(f"Error during data loading: {str(e)}")

if __name__ == "__main__":
    # Example usage
    logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

    # Example destination
    destination_csv = {'type': 'csv', 'file_path': 'data/transformed_data.csv'}
    destination_db = {'type': 'database', 'engine_string': 'postgresql://user:password@localhost:5432/your_database',
                      'table_name': 'your_table'}

    # Example data (replace with actual transformed data)
    transformed_data = pd.DataFrame({
        'Transformed_Column': [2, 4, 6],
        'Another_Transformed_Column': [14, 15, 16]
    })

    # Example usage with CSV destination
    load_data(transformed_data, destination_csv)

    # Example usage with Database destination
    load_data(transformed_data, destination_db)
