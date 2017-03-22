# sc-airflow-awesome

notes for building the airflow on ec2 AWS Linux

Please kindly read the doc

### What I use

Airflow 1.8, CeleryExecutor, Redis, Celery Flower

### important note

1) never use datetime.now, keep use fix datetime anytime

2) keep versioning for dag id and update the version number if there is any changes

3) keep in mind to set start_date on dag in the future

4) set max_active_runs_per_dag = 1 

5) find ways to sync the dags and config file of master and workers (s3/ git)

6) use `catchup_by_default = False` or keep in mind to use backfill

### plugin

api plugin

https://github.com/teamclairvoyant/airflow-rest-api-plugin

### reference

https://deepumohan.com/tech/setting-up-apache-airflow-on-aws-ec2-instance/


https://stlong0521.github.io/20161023%20-%20Airflow.html


http://site.clairvoyantsoft.com/installing-and-configuring-apache-airflow/

