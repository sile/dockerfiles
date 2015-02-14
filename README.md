Dockerfile置き場
================

Dockerfiles
-----------

## kibana

```bash
$ docker pull centos
$ docker build -t kibana kibana/
$ docker run -it --rm kibana

# another shell
$ curl http://CONTAINER_HOST/kibana
```

チートシート
------------

### 使い捨てでコンテナを起動する

```
$ docker run -it --rm IMAGE /bin/bash
```
