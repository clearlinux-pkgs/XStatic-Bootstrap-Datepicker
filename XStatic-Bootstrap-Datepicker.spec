#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Bootstrap-Datepicker
Version  : 1.3.1.0
Release  : 9
URL      : https://pypi.python.org/packages/source/X/XStatic-Bootstrap-Datepicker/XStatic-Bootstrap-Datepicker-1.3.1.0.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-Bootstrap-Datepicker/XStatic-Bootstrap-Datepicker-1.3.1.0.tar.gz
Summary  : Bootstrap-Datepicker 1.3.1 (XStatic packaging standard)
Group    : Development/Tools
License  : Apache-2.0
Requires: XStatic-Bootstrap-Datepicker-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-Bootstrap-Datepicker
--------------
Bootstrap-Datepicker JavaScript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-Bootstrap-Datepicker package.
Group: Default

%description python
python components for the XStatic-Bootstrap-Datepicker package.


%prep
%setup -q -n XStatic-Bootstrap-Datepicker-1.3.1.0

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
