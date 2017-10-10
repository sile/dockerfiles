# See:
# - http://jaeger.readthedocs.io/en/latest/getting_started/
# - https://medium.com/opentracing/take-opentracing-for-a-hotrod-ride-f6e3141f7941
FROM golang:1.9

RUN go get github.com/uber/jaeger
WORKDIR $GOPATH/src/github.com/uber/jaeger
RUN make install_examples
WORKDIR examples/hotrod

CMD go run ./main.go all
