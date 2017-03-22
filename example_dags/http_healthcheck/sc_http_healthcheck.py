"""
### HTTP Health check
### Keep Calling gitHub API and check the callback
"""
from airflow import DAG
from airflow.operators import SimpleHttpOperator, HttpSensor, EmailOperator, DummyOperator
from datetime import datetime, timedelta
import json

default_args = {
    'owner': 'eddieli',
    'depends_on_past': False,
    'start_date': datetime(2017, 3, 14),
    'email': ['email@email.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('sc_http_healthcheck_v2', default_args=default_args, 
schedule_interval='*/10 * * * *')

dag.doc_md = __doc__

t1 = SimpleHttpOperator(
    task_id='get_peter_api',
    http_conn_id='http_gitapi',
    method='GET',
    endpoint='users/peter',
    data=json.dumps({"priority": 5}),
    headers={"Content-Type": "application/json"},
    response_check=lambda response: True if response.json()['login'] == 'peter' else False,
    dag=dag)


t2 = SimpleHttpOperator(
    task_id='get_paul_api',
    http_conn_id='http_gitapi',
    method='GET',
    endpoint='users/paul',
    data=json.dumps({"priority": 5}),
    headers={"Content-Type": "application/json"},
    response_check=lambda response: True if response.json()['login'] == 'paul' else False,
    dag=dag)

t3 = SimpleHttpOperator(
    task_id='get_mary_api',
    http_conn_id='http_gitapi',
    method='GET',
    endpoint='users/mary',
    data=json.dumps({"priority": 5}),
    headers={"Content-Type": "application/json"},
    response_check=lambda response: True if response.json()['login'] == 'Mary' else False,
    dag=dag)


sensor = HttpSensor(
    task_id='check_if_git_exists',
    http_conn_id='http_gitapi',
    endpoint='',
    params={},
    poke_interval=5,
    dag=dag)

t1.set_upstream(sensor)
t2.set_upstream(sensor)
t3.set_upstream(sensor)


