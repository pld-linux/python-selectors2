#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (for Python 3.3, 3.4)

Summary:	Back-ported, durable, and portable selectors
Summary(pl.UTF-8):	Zbackportowane, trwałe i przenośne selektory
Name:		python-selectors2
Version:	2.0.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/selectors2/
Source0:	https://files.pythonhosted.org/packages/source/s/selectors2/selectors2-%{version}.tar.gz
# Source0-md5:	77089bc7a640bf09f784cc029195c24a
URL:		https://pypi.org/project/selectors2/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock >= 2.0.0
BuildRequires:	python-nose >= 1.3.7
BuildRequires:	python-psutil >= 5.2.2
%if "%{py_ver}" < "2.7"
BuildRequires:	python-unittest2
%endif
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-modules < 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-mock >= 2.0.0
BuildRequires:	python3-nose >= 1.3.7
BuildRequires:	python3-psutil >= 5.2.2
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backported, durable, and portable selectors designed to replace the
standard library selectors module.

%description -l pl.UTF-8
Zbackportowane, trwałe i przenośne selektory, zaprojektowane w celu
zastąpienia modułu biblioteki standardowej selectors.

%package -n python3-selectors2
Summary:	Back-ported, durable, and portable selectors
Summary(pl.UTF-8):	Zbackportowane, trwałe i przenośne selektory
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-selectors2
Backported, durable, and portable selectors designed to replace the
standard library selectors module.

%description -n python3-selectors2 -l pl.UTF-8
Zbackportowane, trwałe i przenośne selektory, zaprojektowane w celu
zastąpienia modułu biblioteki standardowej selectors.

%prep
%setup -q -n selectors2-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver} tests/test_selectors2.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} tests/test_selectors2.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py_sitescriptdir}/selectors2.py[co]
%{py_sitescriptdir}/selectors2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-selectors2
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/selectors2.py
%{py3_sitescriptdir}/__pycache__/selectors2.cpython-*.py[co]
%{py3_sitescriptdir}/selectors2-%{version}-py*.egg-info
%endif
