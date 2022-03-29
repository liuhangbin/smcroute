Name: smcroute
Version: 2.5.4
Release: 1%{?dist}
Summary: A static multicast routing daemon

License: GPLv2
URL: https://github.com/troglobit/smcroute
Source0: https://github.com/troglobit/smcroute/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconf-pkg-config
BuildRequires: libcap-devel

%description
SMCRoute is a static multicast routing daemon providing fine grained control
over the multicast forwarding cache (MFC) in the UNIX kernel.

%prep
%autosetup

%build
./autogen.sh
%configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var
%make_build

%install
%{make_install}

%files
%{_sbindir}/smcroute
%{_sbindir}/smcrouted
%{_sbindir}/smcroutectl
%{_mandir}/man5/smcroute.conf.5*
%{_mandir}/man8/smcrouted.8*
%{_mandir}/man8/smcroutectl.8*
%doc README.md
%doc smcroute.conf
%doc COPYING
%{_unitdir}/smcroute.service

%changelog
* Tue Mar 29 2022 Hangbin Liu <haliu@redhat.com> - 2.5.4-1
- Init version
