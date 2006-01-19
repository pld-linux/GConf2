#
# TODO:
# - install evoldap.scheme ?
#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	GNOME2 configuration database system
Summary(pl):	System konfiguracyjnej bazy danych dla GNOME 2
Summary(pt_BR):	Sistema de Configuração do GNOME 2
Summary(ru):	óÉÓÔÅÍÁ ËÏÎÆÉÇÕÒÁÃÉÉ GNOME 2
Name:		GConf2
Version:	2.12.1
Release:	3
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/GConf/2.12/GConf-%{version}.tar.bz2
# Source0-md5:	247110de013ed24b17cf4191eb6daec5
Source1:	%{name}-merge-tree.xinit
Patch0:		%{name}-NO_MAJOR_VERSION.patch
Patch1:		%{name}-path.patch
URL:		http://www.gnome.org/
BuildRequires:	ORBit2-devel >= 1:2.12.3
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.8.3
BuildRequires:	gtk-doc >= 1.4-2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.21
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
Requires:	pkgconfig
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

%prep
%setup -q -n GConf-%{version}
%patch0 -p1
%patch1 -p1

%build
rm -f acinclude.m4
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_static_libs:--disable-static} \
%ifarch ppc
	--disable-gtk-doc
%else
	--enable-gtk-doc
%endif

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
%attr(755,root,root) %{_libdir}/GConf2/lib*.so
%{_sysconfdir}/gconf
%attr(755,root,root) %{_sysconfdir}/X11/xinit/xinitrc.d/*
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
