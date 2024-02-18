import pandas as pd
import logging

def transform_data(data, transformations):
    """
    Transform data based on specified operations.

    Parameters:
    - data: pandas.DataFrame, Input data to be transformed.
    - transformations: List of dictionaries containing transformation details.
                      Example: [{'column': 'Original_Column', 'operation': 'multiply', 'factor': 2},
                                {'column': 'Another_Column', 'operation': 'add', 'value': 10}]

    Returns:
    - pandas.DataFrame: Transformed data.
    """
    transformed_data = data.copy()

    try:
        for transformation in transformations:
            column = transformation.get('column')
            operation = transformation.get('operation')

            if operation == 'multiply':
                factor = transformation.get('factor', 1)
                transformed_data[column] *= factor
            elif operation == 'add':
                value = transformation.get('value', 0)
                transformed_data[column] += value
            else:
                logging.warning(f"Unsupported operation: {operation}. Skipping.")

        logging.info("Data transformation completed successfully.")
        return transformed_data

    except Exception as e:
        logging.error(f"Error during data transformation: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

    # Example transformations
    transformations = [
        {'column': 'Original_Column', 'operation': 'multiply', 'factor': 2},
        {'column': 'Another_Column', 'operation': 'add', 'value': 10}
    ]

    # Example data (replace with actual data source)
    input_data = pd.DataFrame({
        'Original_Column': [1, 2, 3],
        'Another_Column': [4, 5, 6]
    })

    transformed_data = transform_data(input_data, transformations)

    if transformed_data is not None:
        print("Data transformed successfully:")
        print(transformed_data.head())
    else:
        print("Data transformation failed.")
