Summary:	C++ interface to GNOME libraries
Summary(pl):	Interfejs w C++ do bibliotek GNOME
Name:		gnomemm
Version:	1.2.1
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp1.sourceforge.net/gtkmm/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fix.patch
Patch1:		%{name}-am_fix.patch
URL:		http://gtkmm.sourceforge.net/
Requires:	cpp
BuildRequires:	esound-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRequires:	zlib-devel
BuildRequires:	gtkmm-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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
Requires:	gtk+-devel
Requires:	gtkmm-devel
Requires:	gnome-libs-devel

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
%setup -q
%patch0 -p1
%patch1

%build
rm -f missing
libtoolize --copy --force
aclocal -I %{_aclocaldir}/gnome
autoconf
automake -a -c -f
CXXFLAGS="%{rpmcflags} -fno-exceptions"
%configure \
	--enable-static=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -dpr examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}

gzip -9nf README ChangeLog AUTHORS NEWS

# --- start examples ---
cat $RPM_BUILD_ROOT%{_examplesdir}/%{name}/examples.conf.in \
	| sed 's/@SHELL@/\/bin\/sh/g' \
	| sed 's/@CFLAGS@/-O2/g' \
	| sed 's/@CPPFLAGS@/`gnome-config --cflags gnome`/g' \
	| sed 's/@CXXFLAGS@/-O2/g' \
	| sed 's/@CXX@/c++/g' \
	| sed 's/@CXXLD@/c++/g' \
	| sed 's/@GTKMM_CFLAGS@/`gtkmm-config --cflags`/g' \
	| sed 's/@GTKMM_LIBS@/`gtkmm-config --libs`/g' \
	| sed 's/@GNOME_INCLUDEDIR@/`gnome-config --cflags gnome`/g' \
	| sed 's/@GNOMEUI_LIBS@ @GNOME_LIBDIR@/`gnome-config --libs gnome gnomeui`/g' \
	| sed 's/@LIBTOOL@/$(SHELL) \/usr\/bin\/libtool/g' \
	| sed 's/..\/..\/src\/gnome--\/libgnomemm.la/\/usr\/X11R6\/lib\/libgnomemm.la/g' \
	| sed 's/top_builddir = ..\/../top_builddir = ./g' \
	> $RPM_BUILD_ROOT%{_examplesdir}/%{name}/examples.conf
# --- end examples ---

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomemm*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/gnomemmConf.sh

%{_examplesdir}/%{name}

%{_includedir}/*.h
%{_includedir}/gnome--

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
