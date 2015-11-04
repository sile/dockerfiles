Dockerfile置き場
================

Dockerfiles
-----------

## kibana

```bash
$ docker pull centos
$ docker build -t kibana kibana/
$ docker run -it --rm kibana
container$ ip a

# another shell
$ curl -X POST -d 'json={"hoge":"fuga"}&time='`date +%s` http://CONTAINER_HOST:9880/default
$ firefox http://CONTAINER_HOST:5601/
```

必要に応じてtd-agent.confを修正する:
```bash
container$ vim /etc/td-conf/td-agent.conf  # 末尾にkibana/td-agent.conf.templateの内容が追記されているので修正する
container$ service td-agent restart
```


チートシート
------------

### 使い捨てでコンテナを起動する

```
$ docker run -it --rm IMAGE /bin/bash
```

### コンテナを全削除

```
$ docker rm `docker ps -a -q`
```
