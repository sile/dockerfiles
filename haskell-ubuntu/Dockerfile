FROM ubuntu:14.04
MAINTAINER Takeru Ohta <phjgt308@gmail.com>

# apt packages
RUN apt-get update
RUN apt-get install -y zlib1g-dev ghc cabal-install

# update cabal (for cabal sandbox)
RUN cabal update
RUN cabal install cabal-install
RUN ln -fns $HOME/.cabal/bin/cabal /usr/local/bin/cabal
