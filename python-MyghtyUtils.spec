%define		fname		MyghtyUtils
Summary:	Container and Utility Functions from the Myghty Template Framework
Summary(pl):	Funkcje kontenerowe i narzêdziowe z Myghty Template Framework
Name:		python-%{fname}
Version:	0.52
Release:	0.3
License:	MIT
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/M/MyghtyUtils/%{fname}-%{version}.zip
# Source0-md5:	a15cda5919509024245802f4028b1560
URL:		http://www.myghty.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
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

%description -l pl
Zbiór klas narzêdziowych u¿ywanych przez szablony Myghty. Zawiera:

container - system kontenerowy zapewniaj±cy przechowywanie danych
klucz-warto¶æ niezale¿nie od backendu, obs³uguj±cy pamiêæ, pliki DBM,
pliki p³askie i memcached

buffer - funkcje dla powiêkszaj±cych siê obiektów plikowych

util - ró¿ne funkcje i obiekty narzêdziowe

synchronizer - synchronizacja dla wielu czytaj±cych/jednego pisz±cego
przy u¿yciu muteksów w±tkowych lub plików blokad

session - interfejs do sesji zbudowany w oparciu o kontener, podobnie
jak sesje mod_python; aktualnie wymaga obiektu ¿±dania podobnego do
mod_pythona, powinno siê to zmieniæ na co¶ bardziej ogólnego.

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
%{py_sitescriptdir}/myghtyutils
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
