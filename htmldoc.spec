#
# Conditional build:
%bcond_without	gui	# without FLTK-based GUI
#
Summary:	HTML processing program
Summary(pl.UTF-8):	Program przetwarzający HTML
Name:		htmldoc
Version:	1.8.27
Release:	14
License:	GPL v2 with OpenSSL exception
Group:		Applications/Publishing
Source0:	ftp://ftp.easysw.com/pub/htmldoc/%{version}/%{name}-%{version}-source.tar.bz2
# Source0-md5:	35589e7b8fe9c54e11be87cd5aec4dcc
Patch0:		%{name}-libpng15.patch
Patch1:		htmldoc-1.8.27-fortify-fail.patch
Patch2:		htmldoc-1.8.27-scanf-overflows.patch
URL:		http://www.htmldoc.org/
%{?with_gui:BuildRequires:	xorg-lib-libXpm-devel}
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
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
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
%doc COPYING.txt CHANGES.txt README.txt
%doc doc/htmldoc.html doc/htmldoc-fig*.png doc/htmldoc.p* doc/help.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/htmldoc
