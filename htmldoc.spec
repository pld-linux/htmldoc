Summary:	HTML processing program
Summary(pl):	Program przetwarzaj�cy HTML
Name:		htmldoc
Version:	1.8.19
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%{name}-%{version}-source.tar.bz2
URL:		http://www.easysw.com/htmldoc/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	fltk-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define         _noautoreqdep   libGL.so.1 libGLU.so.1

%description
HTML processing program that generates HTML, PostScript, and PDF files
with a table of contents.

%description -l pl
Program przetwarzaj�cy HTML, kt�ry generuje pliki HTML, PostScript i
PDF ze spisem tre�ci.

%prep
%setup -q

%build
aclocal
%{__autoconf}
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        CPPFLAGS="`pkg-config libpng12 --cflags`";
fi
%configure CXXFLAGS="$CPPFLAGS"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

gzip -9nf CHANGES.txt README.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/htmldoc.html doc/htmldoc.png doc/htmldoc-fig*.png
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/htmldoc
