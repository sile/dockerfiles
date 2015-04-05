%global erl_dest /usr/

Name:     erlang
Version:  OTP17.5
Release:  1.native
Summary:  General-purpose concurrent, garbage-collected programming language and runtime system.
Group:    Development/Languages
License:  ERPL
URL:      http://www.erlang.org
Source:   otp_src_17.5.tar.gz
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Erlang Installation Package

%prep
%setup -q -n otp_src_17.5

%build

OPTS='--enable-threads --enable-smp-support --enable-kernel-pool --enable-hipe --enable-native-libs --without-wx --without-javac --without-megaco --without-asn1 --without-cosEvent --without-cosEventDomain --without-cosFileTransfer --without-cosNotification --without-cosProperty --without-cosTime --without-cosTransactions --without-debugger --without-diameter --without-eldap --without-erl_docgen --without-gs --without-ic --without-mnesia --without-observer --without-ose --without-otp_mibs --without-percept --without-snmp --without-test_server --without-webtool --disable-debug --disable-sctp'

CFLAGS='-msse4.2 -O3' %configure ${OPTS} -prefix=%{erl_dest}

# see: http://erlang.org/pipermail/erlang-questions/2014-April/078460.html
make clean
CFLAGS='-msse4.2 -O3' %configure ${OPTS} -prefix=%{erl_dest}

make -j

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{erl_dest}/bin/*
%{erl_dest}/%{_lib}/erlang/*
