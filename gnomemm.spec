Summary:	C++ interface to GNOME libraries
Summary(pl):	Interfejs w C++ do bibliotek GNOME
Name:		gnomemm
Version:	1.3.10
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp1.sourceforge.net/gtkmm/%{name}-all-%{version}.tar.gz
URL:		http://gtkmm.sourceforge.net/
Requires:	cpp
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm-devel >= 1.3.0
BuildRequires:	libgnomeui-devel
BuildRequires:	libtool >= 1.4.3
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
Requires:	%{name} = %{version}
Requires:	gtk+2-devel
Requires:	gtkmm-devel
Requires:	libgnomeui-devel

%description devel
If you are going to write GNOME programs in C++ you will need this
package. It contains all header files, libraries and some examples.

%description devel -l pl
Je¶li zamierzasz pisaæ programy GNOME w C++ bêdziesz potrzebowa³ tego
pakietu. Zawiera on niezbêdne nag³ówki, biblioteki i trochê
przyk³adów.

%package static
Summary:	gnomemm static libraries
Summary(pl):	Biblioteki statyczne gnomemm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Gnomemm static libraries.

%description static -l pl
Biblioteki statyczne gnomemm.

%prep
%setup -q -n %{name}-all-%{version}

%build
CXXFLAGS="%{rpmcflags}"
%configure \
	--enable-static=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_includedir}/*
#%{_examplesdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
