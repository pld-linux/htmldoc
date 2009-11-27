#
# Conditional build:
%bcond_without	gui	# without FLTK-based GUI
#
%define		snap	r1629
Summary:	HTML processing program
Summary(pl.UTF-8):	Program przetwarzający HTML
Name:		htmldoc
Version:	1.9
Release:	0.1.%{snap}
License:	GPL v2 with OpenSSL exception
Group:		Applications/Publishing
Source0:	ftp://ftp.easysw.com/pub/htmldoc/snapshots/%{name}-%{version}.x-%{snap}.tar.bz2
# Source0-md5:	a5982321cadbadaef9ec59c10733b9df
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
%setup -q -n %{name}-%{version}%{?snap:.x-%{snap}}

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
%doc doc/*.html doc/htmldoc-fig*.png doc/htmldoc.p*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/htmldoc
