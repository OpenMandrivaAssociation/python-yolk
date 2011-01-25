%define module	yolk
%define name	python-%{module}
%define version 0.4.1
%define release %mkrel 1

Summary:	Python package command-line query tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/y/%{module}/%{module}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
Url:		http://tools.assembla.com/yolk/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
Yolk is a Python command-line tool and library for obtaining
information about packages installed by setuptools, easy_install and
distutils (Python 2.5) and for querying PyPI.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
%__install -d -m 755 %{buildroot}%{_mandir}/man1
%__install -m 644 docs/yolk.1 %{buildroot}%{_mandir}/man1/

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc AUTHORS COPYING CREDITS FAQ NEWS README THANKS TODO
%_mandir/man1/yolk.*
