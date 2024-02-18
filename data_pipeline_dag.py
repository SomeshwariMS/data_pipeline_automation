from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator

default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='End-to-End Data Pipeline Automation',
    schedule_interval=timedelta(days=1),  # Adjust as needed
)

def extract_data():
    # Your data extraction logic (e.g., read from sources) here
    print("Extracting data...")

def transform_data(**kwargs):
    # Your data transformation logic here
    ti = kwargs['ti']
    extracted_data = ti.xcom_pull(task_ids='extract_data')
    transformed_data = extracted_data.copy()  # Placeholder transformation
    transformed_data['Transformed_Column'] = transformed_data['Original_Column'] * 2
    return transformed_data

def load_data(**kwargs):
    # Your data loading logic (e.g., write to storage) here
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(task_ids='transform_data')
    print("Loading data to the destination...")
    # Implement the loading process here (e.g., writing to a database)

def check_data_quality():
    # Example: Check data quality before loading
    # Implement your data quality checks (e.g., null values, data completeness)
    print("Checking data quality...")

def decide_branch(**kwargs):
    # Example: Decide the branch based on data quality check
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(task_ids='transform_data')
    
    if transformed_data is not None and not transformed_data.empty:
        return 'load_data_task'
    else:
        return 'end_pipeline_task'

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    provide_context=True,
    dag=dag,
)

check_quality_task = PythonOperator(
    task_id='check_data_quality',
    python_callable=check_data_quality,
    dag=dag,
)

branch_task = BranchPythonOperator(
    task_id='branch_task',
    python_callable=decide_branch,
    provide_context=True,
    dag=dag,
)

load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_data,
    provide_context=True,
    dag=dag,
)

end_pipeline_task = DummyOperator(
    task_id='end_pipeline_task',
    dag=dag,
)

# Define task dependencies
extract_task >> transform_task
transform_task >> check_quality_task
transform_task >> branch_task
check_quality_task >> branch_task
branch_task >> [load_data_task, end_pipeline_task]
