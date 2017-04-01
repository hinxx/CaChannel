Summary: CaChannel Interface to EPICS
Name: python-CaChannel
Version: 3.0.0b1
Release: 1%{?dist}
Source0: CaChannel-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Xiaoqiang Wang <xiaoqiang.wang AT psi DOT ch>
Url: http://pypi.python.org/pypi/cachannel

BuildRequires: python-devel python-setuptools epics-base numpy 
Requires: python-enum34

%description
CaChannel - EPICS Channel Access in Python
==========================================

CaChannel is a Python interface to Channel Access. 

Check out `CaChannel documents <https://cachannel.readthedocs.org>`_ to get started.

* Downloads: https://pypi.python.org/pypi/CaChannel
* Source Repo: https://github.com/CaChannel/CaChannel
* Issue Tracker: https://github.com/CaChannel/CaChannel/issues
* Anaconda: https://anaconda.org/paulscherrerinstitute/cachannel



%prep
%setup -n CaChannel-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)