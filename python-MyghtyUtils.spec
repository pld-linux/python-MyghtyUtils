%define		fname		MyghtyUtils
Summary:	Container and Utility Functions from the Myghty Template Framework
Summary(pl.UTF-8):	Funkcje kontenerowe i narzędziowe z Myghty Template Framework
Name:		python-%{fname}
Version:	0.52
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/M/MyghtyUtils/%{fname}-%{version}.zip
# Source0-md5:	a15cda5919509024245802f4028b1560
URL:		http://www.myghty.org/
BuildRequires:	python >= 1:2.4
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	unzip
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the set of utility classes used by Myghty templating. Included
are:

container - the Containment system providing back-end neutral
key/value storage, with support for in-memory, DBM files, flat files,
and memcached

buffer - some functions for augmenting file objects

util - various utility functions and objects

synchronizer - provides many reader/single writer synchronization
using either thread mutexes or lockfiles

session - provides a Session interface built upon the Container,
similar interface to mod_python session. Currently needs a
mod_python-like request object, this should be changed to something
more generic.

%description -l pl.UTF-8
Zbiór klas narzędziowych używanych przez szablony Myghty. Zawiera:

container - system kontenerowy zapewniający przechowywanie danych
klucz-wartość niezależnie od backendu, obsługujący pamięć, pliki DBM,
pliki płaskie i memcached

buffer - funkcje dla powiększających się obiektów plikowych

util - różne funkcje i obiekty narzędziowe

synchronizer - synchronizacja dla wielu czytających/jednego piszącego
przy użyciu muteksów wątkowych lub plików blokad

session - interfejs do sesji zbudowany w oparciu o kontener, podobnie
jak sesje mod_python; aktualnie wymaga obiektu żądania podobnego do
mod_pythona, powinno się to zmienić na coś bardziej ogólnego.

%prep
%setup -qn %{fname}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/myghtyutils
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
