#
# Conditional build:
%bcond_without	gui	# without FLTK-based GUI
#
Summary:	HTML processing program
Summary(pl.UTF-8):	Program przetwarzający HTML
Name:		htmldoc
Version:	1.8.23
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.easysw.com/pub/htmldoc/%{version}/%{name}-%{version}-source.tar.bz2
# Source0-md5:	f867be6e4bdebf84ca6d58b16e4b839c
Patch0:		%{name}-link.patch
URL:		http://www.easysw.com/htmldoc/
%{?with_gui:BuildRequires:	XFree86-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_gui:BuildRequires:	fltk-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML processing program that generates HTML, PostScript, and PDF files
with a table of contents.

%description -l pl.UTF-8
Program przetwarzający HTML, który generuje pliki HTML, PostScript i
PDF ze spisem treści.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	%{!?with_gui:--without-gui}
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
