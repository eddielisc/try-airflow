# sc-airflow-awesome

notes for building the airflow on ec2 AWS Linux

Please kindly read the doc

### What I use

Airflow 1.8, CeleryExecutor, Redis, Celery Flower

### important note

1) never use datetime.now, keep use fix datetime anytime

2) keep versioning for dag id and update the version number if there is any changes

### plugin

api plugin

https://github.com/teamclairvoyant/airflow-rest-api-plugin