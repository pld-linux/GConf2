Summary:	GNOME2 configuration database system
Summary(pl):	System konfiguracyjnej bazy danych dla GNOME2
Summary(pt_BR):	Sistema de ConfiguraÁ„o do GNOME2
Name:		GConf2
Version:	1.1.6
Release:	1
License:	LGPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaÁıes
Group(pt):	X11/AplicaÁıes
Source0:	ftp://ftp.gnome.org/pub/GNOME/pre-gnome2/sources/GConf/GConf-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	ORBit2-devel
BuildRequires:	bonobo-activation-devel
BuildRequires:	db3-devel
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME2

%description
GConf2 is a configuration database system, functionally similar to the
Windows registry but lots better. :-) It's being written for the
GNOME2 desktop but does not require GNOME2; configure should notice if
GNOME2 is not installed and compile the basic GConf2 library anyway.

%description -l pl
GConf2 jest systemem konfiguracyjnej bazy danych, funkcjonalnie
podobnej do rejestru Windows, ale o wiele lepszej :-). Jest pisana dla
desktopu GNOME2, ale nie wymaga GNOME2; skrypt configure powinien
wykryÊ brak gnome i skompilowaÊ tylko wersjÍ podstawow± GConf2.

%description -l pt_BR
Gconf2 È o sistema de banco de dados de configuraÁ„o do GNOME2.

%package devel
Summary:	GConf2 includes, etc
Summary(pl):	Pliki nag≥Ûwkowe GConf2
Summary(pt_BR):	Sistema de ConfiguraÁ„o do GNOME2 - arquivos para desenvolvimento
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	ORBit2-devel
Requires:	gtk+2-devel
Requires:	bonobo-activation-devel

%description devel
GConf2 includes etc.

%description devel -l pl
Pliki nag≥Ûwkowe GConf2.

%description devel -l pt_BR
Sistema de ConfiguraÁ„o do GNOME2 - arquivos para desenvolvimento.

%package static
Summary:	GConf2 static libraries
Summary(pl):	Biblioteki statyczne GConf2
Summary(pt_BR):	Bibliotecas est·ticas para desenvolvimento com gconf2
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
GConf2 static libraries.

%description static -l pl
Biblioteki statyczne GConf2.

%description static -l pt_BR
Bibliotecas est·ticas para desenvolvimento com gconf

%prep
%setup -q -n GConf-%{version}

%build
%configure \
	--enable-gtk-doc=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_aclocaldir},%{_sysconfdir}/gconf/schemas}
install gconf.m4 $RPM_BUILD_ROOT%{_aclocaldir}/gconf-2.m4

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}
	
gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-2
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/GConf
%dir %{_libdir}/GConf/2
%attr(755,root,root) %{_libdir}/GConf/2/lib*.??
%{_sysconfdir}/gconf

%files devel
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_libdir}/lib*.??
%{_includedir}/gconf
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/GConf/2/lib*.a
%{_libdir}/lib*.a
