# notes for airflow 1.8

put upstart folder script in /etc/init/

## related start/ stop command

### Master
```
sudo initctl stop airflow-scheduler
sudo initctl start airflow-scheduler
```
```
sudo initctl stop airflow-flower
sudo initctl start airflow-flower
```
```
sudo initctl stop airflow-webserver
sudo initctl start airflow-webserver
```

### worker
```
sudo initctl stop airflow-worker
sudo initctl start airflow-worker
```
