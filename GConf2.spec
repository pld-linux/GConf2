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
Version:	2.26.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/GConf/2.26/GConf-%{version}.tar.bz2
# Source0-md5:	b010f0de356ea093c6a73778b13de956
Patch0:		%{name}-NO_MAJOR_VERSION.patch
Patch1:		%{name}-reload.patch
URL:		http://www.gnome.org/
BuildRequires:	ORBit2-devel >= 1:2.14.9
BuildRequires:	PolicyKit-devel >= 0.9
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	glib2-devel >= 1:2.19.0
BuildRequires:	gtk+2-devel >= 2:2.15.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post):	findutils
Requires:	%{name}-libs = %{version}-%{release}
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

%package libs
Summary:	GConf2 shared library
Summary(pl.UTF-8):	Biblioteka współdzielona GConf2
Group:		Libraries
Requires:	ORBit2 >= 1:2.14.9
Requires:	glib2 >= 1:2.19.0
Conflicts:	GConf2 < 2.24.0-2

%description libs
GConf2 shared library and gconftool utility (used both for
configuration management and development purposes).

%description libs -l pl.UTF-8
Biblioteka współdzielona GConf2 oraz narzędzie gconftool (używane
zarówno przy zarządzaniu konfiguracją, jak i tworzeniu
oprogramowania).

%package devel
Summary:	Header files for GConf2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GConf2
Summary(pt_BR.UTF-8):	Sistema de Configuração do GNOME2 - arquivos para desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	ORBit2-devel >= 1:2.14.9
Requires:	dbus-devel >= 1.0.0
Requires:	libxml2-devel >= 1:2.6.30
Obsoletes:	libGConf2-devel

%description devel
Header files for GConf2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GConf2.

%description devel -l pt_BR.UTF-8
Sistema de Configuração do GNOME2 - arquivos para desenvolvimento.

%package static
Summary:	GConf2 static libraries
Summary(pl.UTF-8):	Biblioteki statyczne GConf2
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com gconf2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GConf2 static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne GConf2.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com gconf

%package apidocs
Summary:	GConf2 API documentation
Summary(pl.UTF-8):	Dokumentacja API GConf2
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GConf2 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GConf2.

%package examples
Summary:	GConf2 - example programs
Summary(pl.UTF-8):	GConf2 - przykładowe programy
Group:		Development/Libraries
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
	POLKIT_POLICY_FILE_VALIDATE=/usr/bin/polkit-policy-file-validate \
	%{!?with_static_libs:--disable-static} \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}/gconf/{schemas,gconf.xml.system}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp examples/*.schemas $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%find_lang %{name}

# no *.{la,a} for modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/GConf2/lib*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post
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

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gconf-merge-tree
%attr(755,root,root) %{_libexecdir}/gconf-defaults-mechanism
%attr(755,root,root) %{_libexecdir}/gconf-sanity-check-2
%attr(755,root,root) %{_libexecdir}/gconfd-2
%dir %{_libdir}/GConf2
%attr(755,root,root) %{_libdir}/GConf2/libgconfbackend-oldxml.so
%attr(755,root,root) %{_libdir}/GConf2/libgconfbackend-xml.so
%{_sysconfdir}/dbus-1/system.d/org.gnome.GConf.Defaults.conf
%dir %{_sysconfdir}/gconf
%dir %{_sysconfdir}/gconf/2
%{_sysconfdir}/gconf/gconf.xml.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gconf/path
%dir %{_sysconfdir}/gconf/schemas
%{_datadir}/PolicyKit/policy/org.gnome.gconf.defaults.policy
%{_datadir}/dbus-1/services/org.gnome.GConf.service
%{_datadir}/dbus-1/system-services/org.gnome.GConf.Defaults.service
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/schema
%{_datadir}/sgml/gconf

%files libs -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgconf-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgconf-2.so.4
%attr(755,root,root) %{_bindir}/gconftool-2
%{_mandir}/man1/gconftool-2.1*

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

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gconf

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files backend-evoldap
%defattr(644,root,root,755)
%doc backends/README.evoldap
%attr(755,root,root) %{_libdir}/GConf2/libgconfbackend-evoldap.so
%{_datadir}/GConf/schema/evoldap.schema
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gconf/2/evoldap.conf
