Summary: The GNU Portable Library Tool
Name:    libtool
Version: 2.4.7
Release: 0.02
License: GPLv2
URL:     http://www.gnu.org/software/libtool/
Source:  http://ftp.gnu.org/gnu/libtool/libtool-%{version}.tar.gz
Patch0:  soname.patch
BuildRequires: autoconf
BuildRequires: automake


%description
GNU Libtool is a set of shell scripts which automatically configure UNIX and
UNIX-like systems to generically build shared libraries. Libtool provides a
consistent, portable interface which simplifies the process of using shared
libraries.

If you are developing programs which will use shared libraries, but do not use
the rest of the GNU Autotools (such as GNU Autoconf and GNU Automake), you
should install the libtool package.

The libtool package also includes all files needed to integrate the GNU
Portable Library Tool (libtool) and the GNU Libtool Dynamic Module Loader
(ltdl) into a package built using the GNU Autotools (including GNU Autoconf
and GNU Automake).


%package ltdl
Summary:  Runtime libraries for GNU Libtool Dynamic Module Loader
Provides: %{name}-libs = %{version}-%{release}
License:  LGPLv2+


%description ltdl
The libtool-ltdl package contains the GNU Libtool Dynamic Module Loader, a
library that provides a consistent, portable interface which simplifies the
process of using dynamic modules.

These runtime libraries are needed by programs that link directly to the
system-installed ltdl libraries; they are not needed by software built using
the rest of the GNU Autotools (including GNU Autoconf and GNU Automake).


%package ltdl-devel
Summary: Tools needed for development using the GNU Libtool Dynamic Module Loader
Requires: %{name}-ltdl = %{version}-%{release}
License:  LGPLv2+


%description ltdl-devel
Static libraries and header files for development with ltdl.


%prep
%autosetup -n libtool-%{version} -p1
autoreconf -v --force

%build
%configure
%make_build


%install
%make_install


%files
%{_infodir}/libtool.info*.gz
%{_mandir}/man1/libtool.1*
%{_mandir}/man1/libtoolize.1*
%{_bindir}/libtool
%{_bindir}/libtoolize
%{_datadir}/aclocal/*.m4
%dir %{_datadir}/libtool
%{_datadir}/libtool/build-aux


%files ltdl
%{_libdir}/libltdl.so.*


%files ltdl-devel
%{_datadir}/libtool
%exclude %{_datadir}/libtool/build-aux
%{_includedir}/ltdl.h
%{_includedir}/libltdl
%{_libdir}/libltdl.so


%changelog
