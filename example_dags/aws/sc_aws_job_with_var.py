"""
### AWS upload
### upload s3 file and send an link to targer user with expired download link
### trigger by variable shortCircuitIsRun in airflow
### example
### airflow variable --set shortCircuitIsRun True/False
"""
from airflow import DAG
from airflow.contrib.hooks import SSHHook
from airflow.contrib.operators import SSHExecuteOperator
from airflow.operators import EmailOperator, S3KeySensor, ShortCircuitOperator
from datetime import datetime, timedelta
from airflow.models import Variable
import json

sshHook = SSHHook(conn_id='aws_worker_ssh')

default_args = {
    'owner': 'eddieli',
    'depends_on_past': False,
    'start_date': datetime(2017, 3, 14),
    #'end_date': datetime(2017, 3, 20, 19, 53, 42)
    'email': ['email@email.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'params': {'aws_bucket': Variable.get('aws_bucket')},
}

dag = DAG('sc_aws_job_with_var_v1', default_args=default_args, 
schedule_interval='*/10 * * * *')

dag.doc_md = __doc__

t0 = ShortCircuitOperator(
    task_id='checkVariable', python_callable=lambda: True if "True" == Variable.get('shortCircuitIsRun') else False, dag=dag)

t1 = SSHExecuteOperator(
    task_id="uploadS3File",
    bash_command="aws s3 cp /home/ec2-user/sample/shortcircuit.txt s3://{{params.aws_bucket}}",
    xcom_push=False,
    ssh_hook=sshHook,
    dag=dag)

t2 = S3KeySensor(
   task_id='checkS3File',
   bucket_key="shortcircuit.txt",
   wildcard_match=True,
   bucket_name='{{params.aws_bucket}}',
   s3_conn_id='my_conn_S3',
   timeout=30,
   poke_interval=5,
   dag=dag)

t3 = SSHExecuteOperator(
    task_id="preSignS3File",
    bash_command="aws s3 presign s3://{{params.aws_bucket}}/shortcircuit.txt --expires 3600",
    xcom_push=True,
    ssh_hook=sshHook,
    dag=dag)

t4= EmailOperator(
   task_id='sendEmail',
   to='email@email.com',
   subject='shortcircuit file is on AWS (expired in an hour)',
   html_content="<a href='{{ task_instance.xcom_pull(task_ids='preSignS3File', key=None) }}'>click me</a>",
   dag=dag
)

t1.set_upstream(t0)
t2.set_upstream(t1)
t3.set_upstream(t2)
t4.set_upstream(t3)