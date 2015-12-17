# Rust Compiler for Static Linking
#
# see: https://doc.rust-lang.org/book/advanced-linking.html#linux
FROM centos:7

MAINTAINER takeru_ohta <phjgt308@gmail.com>

##
## rustc
##
RUN yum -y install vim git gcc gcc-c++ tar cmake make

RUN curl http://www.musl-libc.org/releases/musl-latest.tar.gz | tar xzf -
RUN cd musl-* && ./configure --disable-shared --prefix=/musldist && make -j 2 && make install

RUN curl http://llvm.org/releases/3.7.0/llvm-3.7.0.src.tar.xz | tar xJf -
WORKDIR llvm-3.7.0.src/projects/

RUN curl http://llvm.org/releases/3.7.0/libcxxabi-3.7.0.src.tar.xz | tar xJf -
RUN mv libcxxabi-3.7.0.src libcxxabi

RUN curl http://llvm.org/releases/3.7.0/libunwind-3.7.0.src.tar.xz | tar xJf -
RUN mv libunwind-3.7.0.src libunwind

RUN mkdir libunwind/build
WORKDIR libunwind/build

RUN cmake -DLLVM_PATH=../../.. -DLIBUNWIND_ENABLE_SHARED=0 ..
RUN make -j 2 && cp lib/libunwind.a /musldist/lib/

RUN git clone https://github.com/rust-lang/rust.git /muslrust
WORKDIR /muslrust
RUN ./configure --target=x86_64-unknown-linux-musl --musl-root=/musldist
RUN make -j 2 && make install

##
## cargo
##
WORKDIR /
RUN curl https://static.rust-lang.org/cargo-dist/cargo-nightly-x86_64-unknown-linux-gnu.tar.gz | tar xzf -
RUN cd cargo* && ./install.sh

##
## OpenSSL
##
RUN curl --tlsv1 https://www.openssl.org/source/openssl-1.0.2e.tar.gz | tar xzf -
RUN cd openssl* && ./Configure no-asm --prefix=/musldist os/compiler:/musldist/bin/musl-gcc && \
    make && make install
