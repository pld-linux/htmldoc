Summary:	HTML processing program
Summary(pl):	Program przetwarzaj±cy HTML
Name:		htmldoc
Version:	1.8.22
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%{name}-%{version}-source.tar.bz2
URL:		http://www.easysw.com/htmldoc/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fltk-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
HTML processing program that generates HTML, PostScript, and PDF files
with a table of contents.

%description -l pl
Program przetwarzaj±cy HTML, który generuje pliki HTML, PostScript i
PDF ze spisem tre¶ci.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure CXXFLAGS="$CPPFLAGS"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt doc/htmldoc.html doc/htmldoc.png doc/htmldoc-fig*.png
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/htmldoc
