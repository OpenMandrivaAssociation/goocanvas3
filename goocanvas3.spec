%define major 3
%define libname %mklibname goocanvas %major
%define develname %mklibname -d goocanvas

Name: goocanvas
Version: 0.15
Release: %mkrel 2
Summary: New canvas widget for GTK+ that uses the cairo 2D library
Group: Development/GNOME and GTK+
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: LGPL+
URL: http://sourceforge.net/projects/goocanvas
Source: http://ftp.gnome.org/pub/GNOME/sources/goocanvas/%{name}-%{version}.tar.bz2
BuildRequires: gtk+2-devel
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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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

%description -n %{develname}
This package contains the development libraries, include files 
and documentation.

%prep
%setup -q

%build
%configure2_5x
%make LIBS=-lm

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README COPYING AUTHORS
%{_libdir}/libgoocanvas.so.%{major}*

%files i18n -f %{name}.lang

%files -n %{develname}
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/%name
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
