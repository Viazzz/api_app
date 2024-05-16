import datetime as dt
from pathlib import Path

import pandas as pd

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook



dag = DAG(
    dag_id="get_data_postgres",
    schedule_interval="@daily",
    start_date=dt.datetime(year=2024, month=5, day=12),
    end_date=dt.datetime(year=2024, month=5, day=16),
    catchup=True,
)

task1 = PostgresOperator(
    task_id = "postgres_read_table",
    postgres_conn_id="postgres_con",
    sql = """
        SELECT id, created, modified, body
        FROM public.apis_operationfact;
    """,
    dag=dag,
)
def _calculate_stats(**context):
    """Calculates event statistics."""
    hook = PostgresHook(postgres_conn_id="postgres_con")
    df = hook.get_pandas_df(sql="""
        SELECT id, created, modified, body
        FROM public.apis_operationfact;
    """)
    output_path = "/data/output/data.csv"
    Path(output_path).parent.mkdir(exist_ok=True)
    df.to_csv(output_path, index=False)
    print(df)

calculate_stats = PythonOperator(
    task_id="to_csv",
    python_callable=_calculate_stats,
    templates_dict={
        "input_path": "/data/events/{{ds}}.json",
        "output_path": "/data/stats/{{ds}}.csv",
    },
    dag=dag,
)
task1 >> calculate_stats
