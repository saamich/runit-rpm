# What the?

runit for use in docker container with my_init

## Base on https://github.com/imeyer/runit-rpm

## Building

```
yum -q -y install rpmdevtools git glibc-static
yum -q -y groupinstall "Development Tools"
git clone https://github.com/saamich/runit-rpm.git runit-rpm
cd ./runit-rpm
./build.sh
sudo rpm -i ~/rpmbuild/RPMS/*/*.rpm
```
