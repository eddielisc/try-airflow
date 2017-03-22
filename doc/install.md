# install or update guideline

### airflow 1.8 feature

https://github.com/apache/incubator-airflow/blob/master/UPDATING.md

### install 1.8 script (pip already have 1.8, deprecated)

```
sudo yum install gcc-c++ python-devel python-setuptools
sudo /usr/local/bin/pip2.7 install lxml
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
wget "https://dist.apache.org/repos/dist/dev/incubator/airflow/airflow-1.8.0rc5+apache.incubating.tar.gz"
tar -xzvf airflow-1.8.0rc5+apache.incubating.tar.gz
cd airflow-1.8.0rc5+apache.incubating
sudo /usr/bin/python setup.py install 
```

### update from 1.7 to 1.8

1) uninstall and install airflow

```
pip uninstall airflow
pip install airflow==1.8
```

2) update the config file according to

https://github.com/apache/incubator-airflow/blob/master/UPDATING.md

```
airflow upgradedb
```

 
