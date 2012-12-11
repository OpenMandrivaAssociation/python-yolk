%define module	yolk

Summary:	Python package command-line query tool
Name:		python-%{module}
Version:	0.4.3
Release:	1
Source0:	http://pypi.python.org/packages/source/y/%{module}/%{module}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
Url:		http://tools.assembla.com/yolk/
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
Yolk is a Python command-line tool and library for obtaining
information about packages installed by setuptools, easy_install and
distutils (Python 2.5) and for querying PyPI.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
%__install -d -m 755 %{buildroot}%{_mandir}/man1
%__install -m 644 docs/yolk.1 %{buildroot}%{_mandir}/man1/
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc AUTHORS COPYING CREDITS FAQ NEWS README THANKS TODO
%_mandir/man1/yolk.*


%changelog
* Tue Jan 25 2011 Lev Givon <lev@mandriva.org> 0.4.1-1mdv2011.0
+ Revision: 632569
- import python-yolk


