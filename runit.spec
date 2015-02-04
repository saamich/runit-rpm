#
# spec file for package runit (Version 2.1.2)
#
# Copyright (c) 2010 Ian Meyer <ianmmeyer@gmail.com>

## This package understands the following switches:
## --with dietlibc ...  statically links against dietlibc

Name:           runit
Version:        2.1.2
Release:        docker%{?_with_dietlibc:diet}%{?dist}

Group:          System/Base
License:        BSD

# Fix _bindir
%define _bindir /usr/bin

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Url:            http://smarden.org/runit/
Source0:        http://smarden.org/runit/runit-%{version}.tar.gz
Patch:          runit-2.1.2-etc-service.patch

Obsoletes: runit <= %{version}-%{release}
Provides: runit = %{version}-%{release}

BuildRequires: make gcc
%if 0%{?rhel} >= 6
BuildRequires:  glibc-static
%endif

%{?_with_dietlibc:BuildRequires:        dietlibc}

Summary:        A UNIX init scheme with service supervision

%description
runit is a cross-platform Unix init scheme with service supervision; a
replacement for sysvinit and other init schemes. It runs on GNU/Linux, *BSD,
Mac OS X, and Solaris, and can easily be adapted to other Unix operating
systems. runit implements a simple three-stage concept. Stage 1 performs the
system's one-time initialization tasks. Stage 2 starts the system's uptime
services (via the runsvdir program). Stage 3 handles the tasks necessary to
shutdown and halt or reboot.

Authors:
---------
    Gerrit Pape <pape@smarden.org>

%prep
%setup -q -n admin/%{name}-%{version}
pushd src
echo "%{?_with_dietlibc:diet -Os }%__cc $RPM_OPT_FLAGS" >conf-cc
echo "%{?_with_dietlibc:diet -Os }%__cc -Os -pipe"      >conf-ld
popd
%patch

%build
sh package/compile

%install
for i in $(< package/commands) ; do
    %{__install} -D -m 0755 command/$i %{buildroot}%{_bindir}/$i
done
%{__install} -d -m 0755 %{buildroot}/etc/service
%{__rm} -rf %{buildroot}%{_bindir}/runit-init
%{__rm} -rf %{buildroot}%{_bindir}/runit

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/chpst
%{_bindir}/runsv
%{_bindir}/runsvchdir
%{_bindir}/runsvdir
%{_bindir}/sv
%{_bindir}/svlogd
%{_bindir}/utmpset
%dir /etc/service

%changelog
* Thu Aug 21 2014 Savinov Artem <asavinov@asdco.ru> 2.1.2-docker
- Initial release for use in docker with my_init 

* Thu Aug 21 2014 Chris Gaffney <gaffneyc@gmail.com> 2.1.2-1
- Initial release of 2.1.2

* Fri Jan 20 2012 Joe Miller <joeym@joeym.net> 2.1.1-6
- modified spec to build on centos-5 (by only requiring glibc-static on centos-6)

* Wed Oct 26 2011 Karsten Sperling <mail@ksperling.net> 2.1.1-5
- Optionally shut down cleanly even on TERM
- Don't call rpm in preun, it can cause problems
- Upstart / inittab tweaks

* Wed Jul 20 2011 Robin Bowes <robin.bowes@yo61.com> 2.1.1-4
-  2.1.1-3 Add BuildRequires
-  2.1.1-4 Support systems using upstart

* Sun Jan 23 2011 ianmmeyer@gmail.com
- Make compatible with Redhat based systems
