# sc-airflow-awesome

notes for building the airflow on ec2 AWS Linux

Please kindly read the doc

### What I use

Airflow 1.8, CeleryExecutor, Redis, Celery Flower

### important note

1) never use datetime.now

2) keep versioning for dag id 

dag = DAG('sc_aws_job_with_conf_v1', default_args=default_args, 
schedule_interval=None)


### plugin

api plugin

https://github.com/teamclairvoyant/airflow-rest-api-plugin