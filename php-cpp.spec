%global commit c083e812b740931bf1e72b1aeec1d27257a71ec0
%global gittag GIT-TAG
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global source_date_epoch_from_changelog 0

Name:           php-cpp
Version:        2.4.12
Release:        2%{?dist}
Summary:        PHP C++ bindings for modules

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://www.php-cpp.com/
Source0:        PHP-CPP-%{version}.tar.gz
Patch0:         support-destdir.patch 
Patch1:         php-8.5-compilation.patch

BuildRequires:  php-devel automake
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

%description
PHP-CPP extension library

%package devel
Summary:                Development library and header files for php-cpp
Group:                  Development/Libraries
Requires:               php-cpp = %{version}-%{release}

%description devel
PHP-CPP development files

%prep
%setup -q -n PHP-CPP-%{version}
%patch -P 0 -p0
%patch -P 1 -p1

%build
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}/%{_libdir}/libphpcpp.a*

%files
%{_libdir}/libphpcpp*

%files devel
%defattr(-,root,root,-)
%{_includedir}/phpcpp/*h
%{_includedir}/phpcpp.h

%changelog


