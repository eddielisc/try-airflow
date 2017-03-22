# Activate authentication 

1) edit airflow.cfg

under [webserver]
```
authenticate = True
auth_backend = airflow.contrib.auth.backends.password_auth
```

2) go to airflow and run following script

> python

```
import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
user = PasswordUser(models.User())
user.username = 'demo'
user.email = 'demo@demo.com'
user.password = 'demo'
session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()
```

3) restart everything
