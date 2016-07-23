Summary:	Shared functions for Ayatana Indicator Display Objects (GTK+ 2.x version)
Summary(pl.UTF-8):	Funkcje współdzielone dla obiektów wyświetlania wskaźników Ayatana (wersja dla GTK+ 2.x)
Name:		ido-gtk2
# note: versions > 0.3.x no longer support GTK+ 2
Version:	0.3.4
Release:	1
License:	LGPL v2.1 or LGPL v3
Group:		Libraries
#Source0Download: https://launchpad.net/ido/+download
Source0:	https://launchpad.net/ido/0.3/%{version}/+download/ido-%{version}.tar.gz
# Source0-md5:	8853b5ca54f1bc6f2a49f3423ea03b25
Patch0:		ido-dont_use_ubuntu_gtk_widget_set_has_grab.patch
URL:		https://launchpad.net/ido
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	gtk+2-devel >= 2:2.20
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	which
Requires:	gtk+2 >= 2:2.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shared functions for Ayatana Indicator Display Objects (GTK+ 2.x
version).

%description -l pl.UTF-8
Funkcje współdzielone dla obiektów wyświetlania wskaźników Ayatana
(wersja dla GTK+ 2.x).

%package devel
Summary:	Development files for ido library (GTK+ 2.x version)
Summary(pl.UTF-8):	Pliki programistyczne biblioteki ido (wersja dla GTK+ 2.x)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.20

%description devel
This package contains the header files for developing applications
that use ido library (GTK+ 2.x version).

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę ido (w wersji dla GTK+ 2.x).

%prep
%setup -q -n ido-%{version}
%patch0 -p1

# gtk+ deprecations
%{__sed} -i -e 's|-Werror||g' src/Makefile.am

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# build only gtk+2 version from this spec; gtk+3 version is built from newer ido in ido-gtk3.spec
%configure \
	--disable-maintainer-flags \
	--disable-silent-rules \
	--with-gtk=2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libido-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libido-0.1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libido-0.1.so
%{_includedir}/libido-0.1
%{_pkgconfigdir}/libido-0.1.pc
