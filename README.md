# sloth
A crawler task management and data demonstration frontend in RESTful Django.


## job management
Tasks are maintained in database with celery beating service

### start redis
install redis and then
```shell
redis-server
redis-cli <<EOF
CONFIG SET protected-mode no
EOF
```

### start a worker
```shell
python manage.py celery -A sloth worker --loglevel=info
```
or
```shell
celery -A sloth worker --loglevel=info
```

### start a beat service to schedule periodic tasks
```shell
celery -A sloth beat -l info
```

### run tasks in shell
```shell
$ python manage.py shell
>>> from job.tasks import add
>>> add.delay(2, 2)
```

## data demonstration
TODO
