%define module nab_provider

Name:		python-nab-provider
Version:	0.0.21
Release:	1
Summary:	IO-free resolution core for nab
License:	MIT
Group:		Development/Python
URL:		https://github.com/notatallshaw/nab
Source0:	https://files.pythonhosted.org/packages/source/n/nab-provider/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)

%description
Resolution provider for nab. It does no network or filesystem IO.
nab 0.0.21 requires this exact version, along with the rest of the stack.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
