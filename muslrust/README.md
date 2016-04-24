muslrust
========

Docker イメージのビルド
--------------------

Dockerfile の [`ARG` 命令](https://docs.docker.com/engine/reference/builder/#arg) を使用しているため、ビルドには Docker 1.9.0 か、それ以降のバージョンが必要。

Dockerfile で定義されたデフォルトの Rust バージョンと、make オプション（`-j 2`）でビルドする場合。

```
cd dockerfiles
docker build -t muslrust muslrust/
```

デフォルトとは別の Rust バージョンと、make オプションでビルドする場合。

```
cd dockerfiles
docker build -t muslrust:1.8.0 --build-arg RUST_VER=1.8.0 --build-arg MAKE_OPTS="-j 4" muslrust/
```
