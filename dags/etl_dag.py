import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import date, timedelta
import os
# TODO: put config and etl.py into a module or outside of dags/
from config import *
from etl import extract, transform, create_report

# set up DAG, https://airflow.apache.org/tutorial.html#default-arguments
default_args = {
    'start_date': airflow.utils.dates.days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'schedule_interval':"@once"
}
dag = DAG('etl_dag', default_args = default_args)

def test_func():
    ''' general debugging'''
    print(os.listdir('.'))
    print(f'SOURCE_PATH: {SOURCE_PATH}')
    print(f'RAW_PATH: {RAW_PATH}')
    print(f'FINAL_PATH: {FINAL_PATH}')
    print(f'REPORTS_PATH: {REPORTS_PATH}')

# set up tasks, https://airflow.apache.org/tutorial.html#tasks
test = PythonOperator(
    task_id='test',
    python_callable=test_func,
    dag=dag)

extract_task = PythonOperator(
    task_id = 'extract',
    python_callable = extract,
    dag=dag)

transform_task = PythonOperator(
    task_id = 'transform',
    python_callable = transform,
    dag=dag)

report_task = PythonOperator(
    task_id = 'report',
    python_callable = create_report,
    dag=dag)

# set up dependencies , https://airflow.apache.org/tutorial.html#setting-up-dependencies
extract_task >> transform_task >> report_task