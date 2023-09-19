#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-zope.configuration
Version  : 5.0
Release  : 55
URL      : https://files.pythonhosted.org/packages/f7/ef/06e1600ed7102e1a8c81993c028d90d6da1e1283c25e99a618c353194244/zope.configuration-5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f7/ef/06e1600ed7102e1a8c81993c028d90d6da1e1283c25e99a618c353194244/zope.configuration-5.0.tar.gz
Summary  : Zope Configuration Markup Language (ZCML)
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-zope.configuration-license = %{version}-%{release}
Requires: pypi-zope.configuration-python = %{version}-%{release}
Requires: pypi-zope.configuration-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(zope.i18nmessageid)
BuildRequires : pypi(zope.interface)
BuildRequires : pypi(zope.schema)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
``zope.configuration``
======================
.. image:: https://img.shields.io/pypi/v/zope.configuration.svg
:target: https://pypi.python.org/pypi/zope.configuration/
:alt: Latest Version

%package license
Summary: license components for the pypi-zope.configuration package.
Group: Default

%description license
license components for the pypi-zope.configuration package.


%package python
Summary: python components for the pypi-zope.configuration package.
Group: Default
Requires: pypi-zope.configuration-python3 = %{version}-%{release}

%description python
python components for the pypi-zope.configuration package.


%package python3
Summary: python3 components for the pypi-zope.configuration package.
Group: Default
Requires: python3-core
Provides: pypi(zope.configuration)
Requires: pypi(setuptools)
Requires: pypi(zope.i18nmessageid)
Requires: pypi(zope.interface)
Requires: pypi(zope.schema)

%description python3
python3 components for the pypi-zope.configuration package.


%prep
%setup -q -n zope.configuration-5.0
cd %{_builddir}/zope.configuration-5.0
pushd ..
cp -a zope.configuration-5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695158868
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zope.configuration
cp %{_builddir}/zope.configuration-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-zope.configuration/a0b53f43aab58b46bf79ba756c50771c605ab4c5 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zope.configuration/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
