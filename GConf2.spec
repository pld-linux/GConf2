#
# TODO:
# - update documentation to follow changes introduced in Patch0
#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	GNOME2 configuration database system
Summary(pl.UTF-8):	System konfiguracyjnej bazy danych dla GNOME 2
Summary(pt_BR.UTF-8):	Sistema de Configuração do GNOME 2
Summary(ru.UTF-8):	Система конфигурации GNOME 2
Name:		GConf2
Version:	2.23.1
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/GConf/2.23/GConf-%{version}.tar.bz2
# Source0-md5:	f0dc9a77c005c9beedd58d70e08cc194
Patch0:		%{name}-NO_MAJOR_VERSION.patch
Patch1:		%{name}-path.patch
Patch2:		%{name}-reload.patch
URL:		http://www.gnome.org/
BuildRequires:	ORBit2-devel >= 1:2.14.9
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.15.6
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post):	findutils
Requires:	ORBit2 >= 1:2.14.9
Requires:	glib2 >= 1:2.15.6
Obsoletes:	GConf2-xinitrc
Obsoletes:	libGConf2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GConf2 is a configuration database system, functionally similar to the
Windows registry but lots better. :-) It's being written for the
GNOME2 desktop but does not require GNOME2; configure should notice if
GNOME2 is not installed and compile the basic GConf2 library anyway.

%description -l pl.UTF-8
GConf2 jest systemem konfiguracyjnej bazy danych, funkcjonalnie
podobnej do rejestru Windows, ale o wiele lepszej :-). Jest pisana dla
desktopu GNOME2, ale nie wymaga GNOME2; skrypt configure powinien
wykryć brak GNOME2 i skompilować tylko wersję podstawową GConf2.

%description -l pt_BR.UTF-8
Gconf2 é o sistema de banco de dados de configuração do GNOME2.

%package apidocs
Summary:	GConf2 API documentation
Summary(pl.UTF-8):	Dokumentacja API GConf2
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GConf2 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GConf2.

%package devel
Summary:	GConf2 includes, etc
Summary(pl.UTF-8):	Pliki nagłówkowe GConf2
Summary(pt_BR.UTF-8):	Sistema de Configuração do GNOME2 - arquivos para desenvolvimento
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ORBit2-devel >= 1:2.14.9
Requires:	libxml2-devel >= 1:2.6.30
Obsoletes:	libGConf2-devel

%description devel
GConf2 includes etc.

%description devel -l pl.UTF-8
Pliki nagłówkowe GConf2.

%description devel -l pt_BR.UTF-8
Sistema de Configuração do GNOME2 - arquivos para desenvolvimento.

%package static
Summary:	GConf2 static libraries
Summary(pl.UTF-8):	Biblioteki statyczne GConf2
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com gconf2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GConf2 static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne GConf2.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com gconf

%package examples
Summary:	GConf2 - example programs
Summary(pl.UTF-8):	GConf2 - przykładowe programy
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
GConf2 - example programs.

%description examples -l pl.UTF-8
GConf2 - przykładowe programy.

%package backend-evoldap
Summary:	Evolution Data Sources LDAP backend for GConf
Summary(pl.UTF-8):	Backend LDAP źródeł danych Evolution dla GConfa
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-evoldap
This is a special-purpose backend for GConf which enables default mail
accounts, addressbooks and calendars for Evolution to be configured
using each user's LDAP entry. By setting each user's mail address,
incoming/outgoing mail server addresses and addressbook/calendar
addresses in the user's LDAP entry, Evolution will be automatically
configured to use these addresses.

%description backend-evoldap -l pl.UTF-8
To jest backend GConfa specjalnego przeznaczenia, pozwalający na
konfigurowanie domyślnych kont pocztowych, książek adresowych i
kalendarzy dla Evolution przy użyciu wpisu LDAP dla każdego
użytkownika. Poprzez ustawienie każdemu użytkownikowi adres pocztowy,
adresy serwerów poczty przychodzącej/wychodzącej oraz adresy książki
adresowej i kalendarza w jego wpisie LDAP, Evolution zostanie
automatycznie skonfigurowane do używania tych adresów.

%prep
%setup -q -n GConf-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
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
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}/gconf/schemas}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp examples/*.schemas $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name}

# no *.{la,a} for modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/GConf2/lib*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
for GCONF_DIR in %{_sysconfdir}/gconf/gconf.xml.mandatory %{_sysconfdir}/gconf/gconf.xml.defaults ;
    do
    GCONF_TREE=$GCONF_DIR/%gconf-tree.xml
    if [ ! -f "$GCONF_TREE" ]; then
	gconf-merge-tree "$GCONF_DIR"
        chmod 644 "$GCONF_TREE"
        find "$GCONF_DIR" -mindepth 1 -maxdepth 1 -type d -exec rm -rf \{\} \;
        rm -f "$GCONF_DIR/%gconf.xml"
    fi
done

%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gconf-merge-tree
%attr(755,root,root) %{_bindir}/gconftool-2
%attr(755,root,root) %{_libdir}/gconf-sanity-check-2
%attr(755,root,root) %{_libdir}/gconfd-2
%attr(755,root,root) %{_libdir}/libgconf-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgconf-2.so.4
%dir %{_libdir}/GConf2
%attr(755,root,root) %{_libdir}/GConf2/libgconfbackend-oldxml.so
%attr(755,root,root) %{_libdir}/GConf2/libgconfbackend-xml.so
%dir %{_sysconfdir}/gconf
%dir %{_sysconfdir}/gconf/2
%{_sysconfdir}/gconf/gconf.xml.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gconf/path
%dir %{_sysconfdir}/gconf/schemas
%{_datadir}/dbus-1/services/org.gnome.GConf.service
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/schema
%{_datadir}/sgml/gconf
%{_mandir}/man1/gconftool-2.1*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gconf

%files devel
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_libdir}/libgconf-2.so
%{_libdir}/libgconf-2.la
%{_includedir}/gconf2
%{_aclocaldir}/gconf-2.m4
%{_pkgconfigdir}/gconf-2.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgconf-2.a
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files backend-evoldap
%defattr(644,root,root,755)
%doc backends/README.evoldap
%attr(755,root,root) %{_libdir}/GConf2/libgconfbackend-evoldap.so
%{_datadir}/GConf/schema/evoldap.schema
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gconf/2/evoldap.conf
