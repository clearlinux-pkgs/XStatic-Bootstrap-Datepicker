#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Bootstrap-Datepicker
Version  : 1.4.0.0
Release  : 25
URL      : https://files.pythonhosted.org/packages/49/58/e42f9a04888a01b1a52ab0a37f13ba219be1074f35d7b16e2ce75200d203/XStatic-Bootstrap-Datepicker-1.4.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/49/58/e42f9a04888a01b1a52ab0a37f13ba219be1074f35d7b16e2ce75200d203/XStatic-Bootstrap-Datepicker-1.4.0.0.tar.gz
Summary  : Bootstrap-Datepicker 1.4.0 (XStatic packaging standard)
Group    : Development/Tools
License  : Apache-2.0
Requires: XStatic-Bootstrap-Datepicker-python = %{version}-%{release}
Requires: XStatic-Bootstrap-Datepicker-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
----------------------------
        
        Bootstrap-Datepicker JavaScript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-Bootstrap-Datepicker package.
Group: Default
Requires: XStatic-Bootstrap-Datepicker-python3 = %{version}-%{release}
Provides: xstatic-bootstrap-datepicker-python

%description python
python components for the XStatic-Bootstrap-Datepicker package.


%package python3
Summary: python3 components for the XStatic-Bootstrap-Datepicker package.
Group: Default
Requires: python3-core
Provides: pypi(xstatic_bootstrap_datepicker)

%description python3
python3 components for the XStatic-Bootstrap-Datepicker package.


%prep
%setup -q -n XStatic-Bootstrap-Datepicker-1.4.0.0
cd %{_builddir}/XStatic-Bootstrap-Datepicker-1.4.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587078295
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
