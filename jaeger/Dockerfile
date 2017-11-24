FROM golang:1.9

RUN curl https://glide.sh/get | sh

RUN go get github.com/jaegertracing/jaeger
WORKDIR $GOPATH/src/github.com/jaegertracing/jaeger
RUN git submodule update --init --recursive
RUN glide install
RUN make

RUN cd cmd/agent/ && go build
RUN cd cmd/collector/ && go build
RUN cd cmd/query/ && go build

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.5/install.sh | bash

WORKDIR /
RUN git clone https://github.com/jaegertracing/jaeger-ui.git
WORKDIR /jaeger-ui
RUN . ~/.nvm/nvm.sh || nvm install 6
RUN . ~/.nvm/nvm.sh && nvm use && npm install -d && npm run build

RUN mkdir /jaeger
WORKDIR /jaeger
RUN cp $GOPATH/src/github.com/jaegertracing/jaeger/cmd/agent/agent .
RUN cp $GOPATH/src/github.com/jaegertracing/jaeger/cmd/collector/collector .
RUN cp $GOPATH/src/github.com/jaegertracing/jaeger/cmd/query/query .
RUN mv /jaeger-ui/build .
