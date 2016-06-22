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

### run tests
```shell
./manage.py test
```

### running in docker
if you have a container that with something running on its port 8000
```shell
docker run -td -P -v /root/work:/home/admin/work -w /home/admin sloth:latest
```
you can run
```shell
wget http://container_ip:8000
```
To get the container´s ip address, run the 2 commands:
```shell
docker ps

docker inspect container_name | grep IPAddress
```
Internally, Docker shells out to call iptables when you run an image, so maybe some variation on this will work.

to expose the container's port 8000 on your localhosts port 8001
```shell
 iptables -t nat -A  DOCKER -p tcp --dport 8000 -j DNAT --to-destination 192.168.42.47:8000
```


## data demonstration
TODO

