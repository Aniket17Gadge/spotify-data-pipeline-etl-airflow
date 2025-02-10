from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from spotify_etl import run_spotify_etl


default_args = {
    'owner' : 'airflow',
    'depends_on_past' : False,
    'Star_date' : datetime(2024, 7, 22),
    'email':['airflow@example.com'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retey_delay': timedelta(minutes=1)
}

#creating The Dag
dag = DAG(
    'spotify_dag',
    default_args=default_args,
    description='My first ETL Data Pipeline'
)

# to Run the dag use python operator
run_etl = PythonOperator(
    task_id = 'complete_spotipy_etl',
    python_callable = run_spotify_etl,
    dag=dag,
    )

run_etl


