# Data Pipeline Automation Project

## Overview

This project focuses on automating the data pipeline to efficiently extract, transform, and load (ETL) data from various sources. The implementation utilizes Apache Airflow for workflow orchestration, pandas for data manipulation, and SQLAlchemy for interacting with databases.

## Key Features

- **Data Extraction:**
  - Flexible script supporting diverse data sources (CSV, JSON).
  - Robust error-handling for seamless extraction processes.

- **Data Transformation:**
  - Versatile transformation script accommodating configurable operations (e.g., multiplication, addition).

- **Data Loading:**
  - Dynamic loading script supporting multiple destination types (CSV files, databases).
  - Error-handling mechanisms for resilient loading processes.

## Usage

1. Ensure dependencies are installed:

    ```bash
    pip install -r requirements.txt
    ```

2. Execute the data pipeline using Apache Airflow:

    ```bash
    airflow scheduler
    airflow webserver -p 8080
    ```

3. Access the Airflow web UI at `http://localhost:8080` and trigger the `data_pipeline` DAG.

## Example Usage

- **Data Extraction:**
    ```python
    python extract_script.py
    ```

- **Data Transformation:**
    ```python
    python transform_script.py
    ```

- **Data Loading:**
    ```python
    python load_script.py
    ```

## Contributions

Contributions and suggestions are welcome. Feel free to submit issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
