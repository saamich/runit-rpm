#!/bin/sh

whereami=$(dirname $0)

if [ ! -f "/etc/rpm/macros.dist" ] && \
   [ ! -f "/etc/rpm/macros.disttag" ];   then echo "please install 'buildsys-macros' rpm and try again" ; exit 1 ; fi
if [ ! -f "$(which rpmbuild)" ];         then echo "please install 'rpm-build' rpm and try again" ; exit 1 ; fi
if [ ! -f "$(which spectool)" ];         then echo "please install 'rpmdevtools' rpm and try again" ; exit 1 ; fi
if [ ! -f "$(which rpmdev-setuptree)" ]; then echo "please install 'rpmdevtools' rpm and try again" ; exit 1 ; fi

# creates ~/rpmbuild
/usr/bin/rpmdev-setuptree

cp -f ${whereami}/runit.spec ~/rpmbuild/SPECS/
cp -f ${whereami}/*.patch    ~/rpmbuild/SOURCES/
curl http://smarden.org/runit/runit-2.1.2.tar.gz > ~/rpmbuild/SOURCES/runit-2.1.2.tar.gz
/usr/bin/spectool -C ~/rpmbuild/SOURCES/ -g ${whereami}/runit.spec 

rpmbuild -bb ~/rpmbuild/SPECS/runit.spec
