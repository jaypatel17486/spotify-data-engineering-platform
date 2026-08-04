from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="spotify_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["spotify", "etl", "aws"],
) as dag:

    run_pipeline = BashOperator(
        task_id="run_spotify_pipeline",
        bash_command="""
        cd /opt/airflow/project &&
        python -m etl.pipeline
        """,
    )