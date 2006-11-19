%define 	module	        myghtyutils
%define     fname           MyghtyUtils
%define     python_version  2.4
Summary:    Container and Utility Functions from the Myghty Template Framework
Name:		python-%{fname}
Version:	0.52
Release:	0.2
License:	MIT
Group:		Libraries/Python
Source0:    http://cheeseshop.python.org/packages/source/M/%{fname}/%{fname}-%{version}.zip
# Source0-md5:   a15cda5919509024245802f4028b1560
URL:		http://www.myghty.org/
BuildRequires:  python-setuptools
BuildRequires:  unzip
Requires:	python >= %{python_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the set of utility classes used by Myghty templating. Included are:

container - the Containment system providing back-end neutral key/value
storage, with support for in-memory, DBM files, flat files, and memcached

buffer - some functions for augmenting file objects

util - various utility functions and objects

synchronizer - provides many reader/single writer synchronization using either
thread mutexes or lockfiles

session - provides a Session interface built upon the Container, similar
interface to mod_python session. Currently needs a mod_python-like request
object, this should be changed to something more generic.

%prep
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{fname}-%{version}-py%{python_version}.egg-info
