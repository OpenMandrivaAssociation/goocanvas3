%define api 2.0
%define major 8
%define oname goocanvas
%define libname %mklibname %oname %api %major
%define develname %mklibname -d %oname %api
Name: goocanvas3
Version: 1.90.0
Release: %mkrel 1
Summary: New canvas widget for GTK+ that uses the cairo 2D library
Group: Development/GNOME and GTK+
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: LGPL+
URL: http://sourceforge.net/projects/goocanvas
Source: http://ftp.gnome.org/pub/GNOME/sources/goocanvas/%{oname}-%{version}.tar.bz2
BuildRequires: gtk+3-devel
BuildRequires: gnome-doc-utils
BuildRequires: intltool

%description
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for 
drawing. It has a model/view split, and uses interfaces for canvas items and 
views, so you can easily turn any application object into canvas items.

%package -n %{libname}
Summary: New canvas widget for GTK+ that uses the cairo 2D library
Group: System/Libraries
Requires: %{name}-i18n >= %{version}
Provides: lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the shared library for goocanvas.

%package i18n
Summary: New canvas widget for GTK+ that uses the cairo 2D library
Group: System/Internationalization

%description i18n
This package contains the translations for goocanvas.

%package -n %{develname}
Summary: New canvas widget for GTK+ that uses the cairo 2D library
Group: Development/GNOME and GTK+
Requires: %{libname} = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: %{oname}-%api-devel = %{version}-%{release}

%description -n %{develname}
This package contains the development libraries, include files 
and documentation.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x
%make LIBS=-lm

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{oname}

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README COPYING AUTHORS
%{_libdir}/libgoocanvas-%api.so.%{major}*

%files i18n -f %{oname}.lang

%files -n %{develname}
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/%name
%{_includedir}/%{name}-%api
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
