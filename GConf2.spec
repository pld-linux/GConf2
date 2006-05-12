#
# TODO:
# - update documentation to follow changes introduced in Patch0
#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	GNOME2 configuration database system
Summary(pl):	System konfiguracyjnej bazy danych dla GNOME 2
Summary(pt_BR):	Sistema de Configuração do GNOME 2
Summary(ru):	óÉÓÔÅÍÁ ËÏÎÆÉÇÕÒÁÃÉÉ GNOME 2
Name:		GConf2
Version:	2.14.0
Release:	2
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/GConf/2.14/GConf-%{version}.tar.bz2
# Source0-md5:	d07c2efcaf477cf34225c604a04b6271
Source1:	%{name}-merge-tree.xinit
Patch0:		%{name}-NO_MAJOR_VERSION.patch
Patch1:		%{name}-path.patch
URL:		http://www.gnome.org/
BuildRequires:	ORBit2-devel >= 1:2.13.2
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.9.0
BuildRequires:	gtk+2-devel >= 2:2.8.3
BuildRequires:	gtk-doc >= 1.4-2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.21
BuildRequires:	openldap-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.197
Obsoletes:	libGConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GConf2 is a configuration database system, functionally similar to the
Windows registry but lots better. :-) It's being written for the
GNOME2 desktop but does not require GNOME2; configure should notice if
GNOME2 is not installed and compile the basic GConf2 library anyway.

%description -l pl
GConf2 jest systemem konfiguracyjnej bazy danych, funkcjonalnie
podobnej do rejestru Windows, ale o wiele lepszej :-). Jest pisana dla
desktopu GNOME2, ale nie wymaga GNOME2; skrypt configure powinien
wykryæ brak GNOME2 i skompilowaæ tylko wersjê podstawow± GConf2.

%description -l pt_BR
Gconf2 é o sistema de banco de dados de configuração do GNOME2.

%package devel
Summary:	GConf2 includes, etc
Summary(pl):	Pliki nag³ówkowe GConf2
Summary(pt_BR):	Sistema de Configuração do GNOME2 - arquivos para desenvolvimento
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ORBit2-devel >= 1:2.12.3
Requires:	gtk-doc-common
Requires:	libxml2-devel >= 1:2.6.21
Obsoletes:	libGConf2-devel

%description devel
GConf2 includes etc.

%description devel -l pl
Pliki nag³ówkowe GConf2.

%description devel -l pt_BR
Sistema de Configuração do GNOME2 - arquivos para desenvolvimento.

%package static
Summary:	GConf2 static libraries
Summary(pl):	Biblioteki statyczne GConf2
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com gconf2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GConf2 static libraries.

%description static -l pl
Biblioteki statyczne GConf2.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com gconf

%package backend-evoldap
Summary:	Evolution Data Sources LDAP backend for GConf
Summary(pl):	Backend LDAP ¼róde³ danych Evolution dla GConfa
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-evoldap
This is a special-purpose backend for GConf which enables default mail
accounts, addressbooks and calendars for Evolution to be configured
using each user's LDAP entry. By setting each user's mail address,
incoming/outgoing mail server addresses and addressbook/calendar
addresses in the user's LDAP entry, Evolution will be automatically
configured to use these addresses.

%description backend-evoldap -l pl
To jest backend GConfa specjalnego przeznaczenia, pozwalaj±cy na
konfigurowanie domy¶lnych kont pocztowych, ksi±¿ek adresowych i
kalendarzy dla Evolution przy u¿yciu wpisu LDAP dla ka¿dego
u¿ytkownika. Poprzez ustawienie ka¿demu u¿ytkownikowi adres pocztowy,
adresy serwerów poczty przychodz±cej/wychodz±cej oraz adresy ksi±¿ki
adresowej i kalendarza w jego wpisie LDAP, Evolution zostanie
automatycznie skonfigurowane do u¿ywania tych adresów.

%prep
%setup -q -n GConf-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}{/gconf/schemas,/X11/xinit/xinitrc.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/GConf2-merge-tree

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

# no *.{la,a} for modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/GConf2/lib*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gconf*
%attr(755,root,root) %{_libdir}/gconf-sanity-check-2
%attr(755,root,root) %{_libdir}/gconfd-2
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/GConf2
%attr(755,root,root) %{_libdir}/GConf2/libgconfbackend-oldxml.so
%attr(755,root,root) %{_libdir}/GConf2/libgconfbackend-xml.so
%dir %{_sysconfdir}/gconf
%dir %{_sysconfdir}/gconf/2
%{_sysconfdir}/gconf/gconf.xml.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gconf/path
%dir %{_sysconfdir}/gconf/schemas
%attr(755,root,root) %{_sysconfdir}/X11/xinit/xinitrc.d/*
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/schema
%{_datadir}/sgml/gconf
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gconf2
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/gconf

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%files backend-evoldap
%defattr(644,root,root,755)
%doc backends/README.evoldap
%attr(755,root,root) %{_libdir}/GConf2/libgconfbackend-evoldap.so
%{_datadir}/GConf/schema/evoldap.schema
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gconf/2/evoldap.conf
