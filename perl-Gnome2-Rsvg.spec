#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gnome2
%define		pnam	Rsvg
Summary:	Perl librsvg bindings
Summary(pl.UTF-8):	Wiązania librsvg dla Perla
Name:		perl-Gnome2-Rsvg
Version:	0.10
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	007b2c9510a3c97f4fce73d1b27372a0
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	librsvg-devel >= 2.16.0
BuildRequires:	perl-Cairo >= 1.00
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-Glib >= 1.140
BuildRequires:	perl-Gtk2 >= 1.140
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	librsvg >= 2.16.0
Requires:	perl-Cairo >= 1.00
Requires:	perl-Glib >= 1.140
Requires:	perl-Gtk2 >= 1.140
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to librsvg library.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do biblioteki librsvg.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/Rsvg/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome2/Rsvg.pm
%dir %{perl_vendorarch}/Gnome2/Rsvg
%{perl_vendorarch}/Gnome2/Rsvg/Install
%dir %{perl_vendorarch}/auto/Gnome2/Rsvg
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Rsvg/*.so
%{perl_vendorarch}/auto/Gnome2/Rsvg/*.bs
%{_mandir}/man3/*
