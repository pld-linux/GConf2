
%define		snap		20030330

Summary:	GNOME2 configuration database system
Summary(pl):	System konfiguracyjnej bazy danych dla GNOME2
Summary(pt_BR):	Sistema de Configuração do GNOME2
Name:		GConf2
Version:	2.3.1
Release:	1.%{snap}
License:	LGPL
Group:		X11/Applications
Source0:	%{name}-%{version}-%{snap}.tar.bz2
#Source0:	http://ftp.gnome.org/pub/GNOME/sources/GConf/2.3/GConf-%{version}.tar.bz2
Patch0:		%{name}-NO_MAJOR_VERSION.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-path.patch
URL:		http://www.gnome.org/
BuildRequires:	ORBit2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-activation-devel >= 2.1.1
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	freetype-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	Xft-devel >= 2.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libGConf2

%description
GConf2 is a configuration database system, functionally similar to the
Windows registry but lots better. :-) It's being written for the
GNOME2 desktop but does not require GNOME2; configure should notice if
GNOME2 is not installed and compile the basic GConf2 library anyway.

%description -l pl
GConf2 jest systemem konfiguracyjnej bazy danych, funkcjonalnie
podobnej do rejestru Windows, ale o wiele lepszej :-). Jest pisana dla
desktopu GNOME2, ale nie wymaga GNOME2; skrypt configure powinien
wykryæ brak gnome i skompilowaæ tylko wersjê podstawow± GConf2.

%description -l pt_BR
Gconf2 é o sistema de banco de dados de configuração do GNOME2.

%package devel
Summary:	GConf2 includes, etc
Summary(pl):	Pliki nag³ówkowe GConf2
Summary(pt_BR):	Sistema de Configuração do GNOME2 - arquivos para desenvolvimento
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	ORBit2-devel
Requires:	bonobo-activation-devel
Requires:	gtk-doc-common
Requires:	libxml2-devel
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
Requires:	%{name}-devel = %{version}

%description static
GConf2 static libraries.

%description static -l pl
Biblioteki statyczne GConf2.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com gconf

%prep
%setup -q
#%%setup -q -n GConf-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1

%build
rm -f missing acinclude.m4
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--with-html-dir=%{_gtkdocdir} \
%ifarch ppc
	--disable-gtk-doc 
%else
	--enable-gtk-doc 
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_aclocaldir},%{_sysconfdir}/gconf/schemas}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir} 
	
install gconf.m4 $RPM_BUILD_ROOT%{_aclocaldir}/gconf-2.m4

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/gconf*
%attr(755,root,root) %{_libdir}/gconf-sanity-check-2
%attr(755,root,root) %{_libdir}/gconfd-2
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/GConf2
%attr(755,root,root) %{_libdir}/GConf2/lib*.so
%{_sysconfdir}/gconf
%{_datadir}/sgml/gconf

%files devel
%defattr(644,root,root,755)
%doc ChangeLog TODO
%doc %{_gtkdocdir}/gconf
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/GConf2/lib*.la
%{_includedir}/gconf2
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/GConf2/lib*.a
%{_libdir}/lib*.a
