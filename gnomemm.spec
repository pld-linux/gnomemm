Summary:	C++ interface to GNOME libraries
Summary(pl):	Interfejs w C++ do bibliotek GNOME
Name:		gnomemm
# There is no release yet, but this package is required by few others (it was
# a part of gtkmm). I've made tarball from GNOME anoncvs.
Version:	0.0.0cvs
Release:	1
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
License:	GPL
Source0:	%{name}-%{version}.tar.gz
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	libsigc++-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtkmm-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	esound-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gnomemm (gnome--) is a C++ interface to GNOME libraries. If you want
to run GNOME programs written in C++ you need gnomemm.

%description -l pl
Gnomemm (gnome--) jest interfejsem do bibliotek GNOME dla C++. Je¶li
chcesz uruchamiaæ programy GNOME napisane w C++ bêdziesz potrzebowa³
tych bibliotek.

%package devel
Summary:	Header files and some examples for gnomemm (gnome--)
Summary(pl):	Pliki nag³ówkowe i przyk³ady dla gnomemm (gnome--)
Group:		X11/Development/Libraries
OARequires:	%{name} = %{version}
Requires:	gnome-libs-devel

%description devel
If you are going to write GNOME programs in C++ you will need this
package. It contains all header files, libraries and some examples.
Unfortunatelly there is no documentation. For more information check
http://gtkmm.sourceforge.net.

%description -l pl devel
Je¶li zamierzasz pisaæ programy GNOME w C++ bêdziesz potrzebowa³ tego
pakietu. Zawiera on niezbêdne nag³ówki, biblioteki i trochê
przyk³adów. Niestety narazie nie zawiera ¿adnej dokumentacji. Wiêcej
informacji znajdziesz na http://gtkmm.sourceforge.net.

%prep
%setup -q -n gnome--

%build
#autoheader;autoconf;automake; 
LDFLAGS="-s" ; export LDFLAGS
# It's easier to not run 'configure' from 'autogen.sh', beacuse we can use
# 'configure' makro, which will pass all required arguments.
NOCONFIGURE="1" ./autogen.sh
%configure \
	--enable-docs

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_usrsrc}/examples/%{name}/gnome-hello
install examples/*.{cc,conf} \
	$RPM_BUILD_ROOT/usr/src/examples/%{name}
install examples/gnome-hello/{Makefile,*.{cc,h,png}} \
	$RPM_BUILD_ROOT/usr/src/examples/%{name}/gnome-hello

gzip -9nf README AUTHORS NEWS ChangeLog

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%doc *.gz

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/gnomemmConf.sh
/usr/src/examples/%{name}
